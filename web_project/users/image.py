from flask_restx import Namespace, Resource
from flask import render_template, redirect, url_for, make_response, request, session, flash, jsonify
from controll.image_model import ImageTable
from PIL import Image
import io
import torch
import io
import argparse
from controll.food_model import food_model
from controll.today_cal import today_cal
import numpy as np


image = Namespace('image')


@ image.route('/')
class Register(Resource):
    def post(self):

        model = torch.hub.load(
            "./yolov5_models/yolov5", "custom", path='./yolov5_models/AFv1.pt', source='local', force_reload=True)
        # 학습시킨 모델 파일을 불러옵니다

        model.eval()

        d = request.files['image']
        data = request.form['user_email']
        # image와 email을 받아옵니다

        user_email = list(filter(lambda x: 'user_email' in x,
                                 data.split(';')))[0].split('=')[1]
        # 쿠키에 저장된 email값이 깔끔하게 들어가 있지 않아서 전처리를 해줍니다

        img_bytes = d.read()

        img = Image.open(io.BytesIO(img_bytes))
        results = model(img, size=640)
        results.render()
        for img in results.imgs:
            img_base64 = Image.fromarray(img)
            filename = d.filename.split('.jpg')
            img_base64.save(
                f"./static/{filename[0]}.jpeg", format="JPEG")
        # 이미지를 모델에 통과시킨 후 해당 이미지를 static 폴더내에 저장합니다

        data = results.pandas().xyxy[0].to_json(orient="records")
        cal = results.pandas().xyxy[0]['class'].values
        # 검출된 음식의 class 번호입니다
        name = results.pandas().xyxy[0]['name'].values
        # 검출된 음식의 이름 정보입니다

        ImageTable.add_image(
            user_email, f'{filename[0]}.jpeg', cal, name)
        # 파일이름, 클래스정보, 이름을 DB에 저장합니다

        result = ImageTable.get_image(user_email)[-1].image
        # 방금 저장된 image의 이름입니다

        result2 = ImageTable.get_image(user_email)[-1].cal
        # 방금 저장된 음식 이미지의 class 번호들입니다

        result3 = food_model.get()
        # 영양데이터가 저장된 DB입니다

        abc = result2[1:-1]
        abc = abc.split()
        temp = []
        for i in abc:
            temp.append(result3[int(i)])
        # 영양데이터의 경우 작성된 csv파일을 그대로 올려서 사용했습니다
        # 음식 이미지의 class 번호와 영양데이터DB의 인덱스가 같은걸 이용해서 전처리 했습니다

        return make_response(jsonify({'result': result, 'result2': result2, 'result3': temp}))


@ image.route('/')
class Register(Resource):
    def put(self):
        # data = 음식이름들
        data = request.form['data']
        # temp_data = 음식이름들을 전처리 한 리스트 입니다
        # 예시 : [김치찌개, 된장찌개]
        temp_data = data.split(',')[1:-1]
        print(temp_data)
        # user_data = 쿠키에 저장되어 있던 email 입니다
        user_data = request.form['user_email']
        # number = 음식 수량입니다
        number = request.form['number']
        # number_data = 음식수량을 전처리 한 리스트 입니다
        # 예시 : [1, 2, 3, 1, 2]
        number_data = number.split(',')[1:-1]

        # 빈 딕셔너리를 하나 생성했습니다
        # data_dict = 음식이름을 키로 수량을 값으로 저장할 용도입니다
        data_dict = {}
        for i in range(len(temp_data)):
            # 음식이름들이 중복으로 검출되는 경우가 많기 때문에 여러 조건들을 추가했습니다
            # 이미 음식이름이 존재한 경우
            if temp_data[i] in data_dict:
                # 현재 저장되어 수량이 많다면 무시합니다
                if int(data_dict[temp_data[i]]) >= int(number_data[i]):
                    pass
                else:
                    # 현재 저장되어 있는 수량보다 큰 수량이 들어온다면 반영합니다
                    data_dict[temp_data[i]] = number_data[i]

            else:
                # 새로운 음식이 들어온 경우도 반영해 줍니다
                data_dict[temp_data[i]] = number_data[i]

        # 이메일도 전처리를 해줍니다
        user_email = list(filter(lambda x: 'user_email' in x,
                                 user_data.split(';')))[0].split('=')[1]

        # result2 = 유저가 가장 최근에 올린 이미지의 class 번호들입니다
        result2 = ImageTable.get_image(user_email)[-1].cal
        # result3 = 영양데이터 정보를 전부 가져옵니다 음식이름과 칼로리 등이 담겨있습니다
        result3 = food_model.get()

        # 클래스 번호들을 다루기 쉽게 전처리 해줍니다
        abc = result2[1:-1]
        abc = abc.split()

        # 새로운 빈 딕셔너리를 만들었습니다
        temp = {}
        # 음식이름 을 키로, 나머지 칼로리부터 영양성분 리스트를 밸류로 잡아줍니다
        for i in abc:
            temp[result3[int(i)][0]] = result3[int(i)][1:]

        # data_dict 에는 음식이름 : 수량 형태로 저장되어 있습니다
        for idx, val in data_dict.items():
            # 음식 수량이 1인분이 아닌경우
            if int(val) != 1:
                # 빈 리스트 생성
                temp2 = []
                # 반복문을 돌면서 칼로리부터 모든 영양소에 수량을 곱해줍니다
                # 예시 : 1인분의 경우 [1, 2, 3, 4, 5] 라면
                # 2인분의 경우 [2, 4, 6, 8, 10] 의 형태로 바뀌게 됩니다
                for i in range(len(temp[idx])):
                    temp2.append(temp[idx][i] * int(val))
                # 이렇게 만들어진 값을 새로 반영해줍니다
                temp[idx] = temp2
        print(temp)

        # sum_cal = [0, 0, 0 ...] 의 넘파이 배열입니다
        # 이곳에 반복문을 돌면서 지금까지 전처리 한 데이터들을 합산해줍니다
        sum_cal = np.array([0] * 14)
        for k in data_dict.keys():
            sum_cal += np.array(temp[k][1:]).astype(int)

        # 연산이 끝났다면 DB에 저장해줍니다
        today_cal.add_cal(user_email, *sum_cal)


@ image.route('/')
class Register(Resource):
    def delete(self):
        # 유저 email을 받아와서 전처리 해줍니다
        user_data = request.form['user_email']
        user_email = list(filter(lambda x: 'user_email' in x,
                                 user_data.split(';')))[0].split('=')[1]
        # 해당 유저의 가장 최근 데이터를 삭제합니다
        today_cal.del_cal(user_email)
