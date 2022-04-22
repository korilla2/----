from flask_restx import Namespace, Resource
from flask import render_template, redirect, url_for, make_response, request, session, flash, send_file
from controll.cal_model import Calorie_model
from controll.user_info_model import user_info_table
from controll.image_model import ImageTable
from controll.today_cal import today_cal
import numpy as np
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import matplotlib.font_manager as fm


mainpage = Namespace('mainpage')


@mainpage.route('/')
class Mainpage(Resource):
    def get(self):
        # 로그인 된 상태인지 확인
        if 'token' in session:
            # 이제 막 가입한 회원의 경우 데이터가 없으므로 오류가 발생합니다
            # 그것을 막기 위해 예외처리를 진행했습니다
            try:
                # 쿠키에서 email을 가지고 와 사용자를 확인합니다
                user_data = request.cookies.get('user_email').split('%40')
                user_email = user_data[0] + '@' + user_data[1]
                print(user_email)
                # 내 정보 DB에 저장된 수치를 찾아봅니다
                user = user_info_table.search(user_email)
                # 그 중 성별과 나이만 뽑아옵니다
                sex = user[-1].sex
                age = user[-1].age
                # result =  나이와 성별로 권장섭취량을 가지고 옵니다
                result = Calorie_model.get(sex, age)
                # temp = 유저가 오늘 저장한 정보를 가지고 옵니다
                temp = today_cal.get_cal(user_email)
                # 정보가 없는 경우를 대비해서 0으로 채운 배열도 생성해줍니다
                efg = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                for i in temp:

                    abc = np.array(
                        [i.number1, i.number2, i.number3, i.number4, i.number5, i.number6, i.number7,
                         i.number8, i.number9, i.number10, i.number11, i.number12,
                         i.number13, i.number14])
                    # DB에서 가져온 데이터들을 합산해줍니다
                    efg += abc

            except:
                # DB에 데이터가 없다면 0으로 보여지게 했습니다
                result = [0] * 20
                efg = [0] * 20

            # 지금까지 계산한 결과를 메인페이지로 전달해줍니다
            return make_response(render_template('mainpage.html', cal_data=result, today_data=efg))
        else:
            return make_response(render_template('login.html'))


@mainpage.route('/login')
class Login(Resource):
    def get(self):
        if 'token' in session:
            return make_response(redirect('http://bp.aidetector.link/mainpage/'))
            # session에 token 이라는 키 값이 있다면 로그인 된 상태로 판단합니다
        else:
            return make_response(render_template('login.html'))
            # session에 token 이라는 키 값이 없다면 login.html을 보여줍니다


@ mainpage.route('/register')
class Register(Resource):
    def get(self):
        if 'token' in session:
            session.pop('token')
        return make_response(render_template('register.html'))


@ mainpage.route('/logout')
class Register(Resource):
    def get(self):
        if 'token' in session:
            session.pop('token')
            return make_response(redirect('http://bp.aidetector.link/mainpage/login'))
        else:
            return make_response(redirect('http://bp.aidetector.link/mainpage/login'))


@ mainpage.route('/info')
class Register(Resource):
    def get(self):
        if 'token' in session:
            # 방금 가입한 유저일 수 있으므로 예외처리를 진행합니다
            try:
                # 현재 로그인한 유저의 email을 가지고 옵니다
                user_data = request.cookies.get('user_email').split('%40')
                user_email = user_data[0] + '@' + user_data[1]
                # 가지고 온 email을 통해서 해당 유저가 최근에 입력시킨 정보값들을 가지고 옵니다
                user = user_info_table.search(user_email)[-1]
            except:
                user = None
            # 해당 정보들을 info.html에 전송합니다
            return make_response(render_template('info.html', user=user))

        # 로그인되지 않은 사용자라 판단되므로 로그인 페이지로 보냅니다
        else:
            return make_response(redirect('http://bp.aidetector.link/mainpage/login'))


@ mainpage.route('/fig')
class Register(Resource):
    def get(self):
        # email을 통해서 해당 유저의 정보를 가지고 와 보여주는 부분입니다
        # 3가지 그래프 중 가장 윗 부분에 해당합니다
        plt.figure(figsize=(6, 7))
        user_data = request.cookies.get('user_email').split('%40')
        user_email = user_data[0] + '@' + user_data[1]
        # user = 현재 로그인 된 사용자의 체중, 신장 등의 정보가 담겨있습니다
        user = user_info_table.search(user_email)

        weight = []
        datetime = []
        # 시간에 따른 몸무게 변화를 그래프로 보여주기 위해
        # 시간과 몸무게를 전처리 해줍니다
        for x in range(len(user)):
            weight.append(user[x].weight)
            datetime.append(str(user[x].datetime.strftime('%Y-%m-%d')))

        # 폰트를 바꾸는 부분입니다
        BMJUA = fm.FontProperties(
            fname='/home/ubuntu/anaconda3/envs/python3/fonts/BMJUA_ttf.ttf')

        # matplotlib 의 pyplot을 이용해 간단한 그림을 그린 뒤 전송하는 부분입니다
        plt.plot(datetime, weight, color='#375bfa')
        plt.plot(datetime, weight, 'go', color='#375bfa')
        plt.title('몸무게 변화', fontsize=30, fontproperties=BMJUA)
        plt.xticks(rotation=30)
        img = BytesIO()
        plt.savefig(img, format='png', dpi=300)
        img.seek(0)

        return send_file(img, mimetype='image/png')


@ mainpage.route('/fig2')
class Register(Resource):
    def get(self):

        plt.figure(figsize=(6, 7))
        user_data = request.cookies.get('user_email').split('%40')
        user_email = user_data[0] + '@' + user_data[1]
        user = today_cal.search(user_email)

        #print('user_email :', user_email)
        #print('user : ',user)
        # print('user[1].number1 : ',user[1].number1)
        # print('user[1] : ',user[1])
        week = []

        for x in range(len(user)):
            user_calory = user[x].number1  # 칼로리
            # user_tansu = user[x].number2 #탄수화물
            # user_jibang = user[x].number4 #지방
            # user_danbak = user[x].number5 #단백질
            datetime = user[x].datetime  # 시간

            day = [user_calory, datetime]

            week.append(list(day))  # 계정에 맞는 칼로리와 탄단지와 시간 정보

        print('week : ', week)

        df = pd.DataFrame(week)
        print(df)
        #print('len(df) :',len(df))
        # print(df.loc[0],df.loc[4])
        #df2 = pd.DataFrame(df.groupby([4]).sum())
        # print(df.groupby([4]).sum())
        # print(df2)
        # print(df2[2])

        df[2] = df.groupby(by=[1])[0].transform(lambda x: x.cumsum())
        print(df)

        ax = plt.subplot()
        ax.bar(df[1], df[2], color='#375bfa')
        ax.xaxis_date()
        # w = 0.15
        # nrow = df.shape[0]
        # idx = np.arange(nrow)
        # for x in ax.patches:
        # height = x.get_height()
        # ax.text(x.get_x() + x.get_width()/2., height+3, height, ha='center', size=10)
        # plt.bar(idx, df[2], width = w)
        # plt.xticks(idx, df[1].dt.date, rotation = 30)
        BMJUA = fm.FontProperties(
            fname='/home/ubuntu/anaconda3/envs/python3/fonts/BMJUA_ttf.ttf')
        plt.title('칼로리 변화', fontsize=30, fontproperties=BMJUA)
        plt.xticks(rotation=30)

        img = BytesIO()
        plt.savefig(img, format='png', dpi=300)
        img.seek(0)
        return send_file(img, mimetype='image/png')


@ mainpage.route('/fig3')
class Register(Resource):
    def get(self):

        plt.figure(figsize=(6, 7))
        user_data = request.cookies.get('user_email').split('%40')
        user_email = user_data[0] + '@' + user_data[1]
        user = today_cal.search(user_email)

        week = []

        for x in range(len(user)):
            # user_calory = user[x].number1 #칼로리
            user_tansu = user[x].number2  # 탄수화물
            user_jibang = user[x].number4  # 지방
            user_danbak = user[x].number5  # 단백질
            datetime = user[x].datetime  # 시간

            day = [user_tansu, user_jibang, user_danbak, datetime]

            week.append(list(day))  # 계정에 맞는 칼로리와 탄단지와 시간

        print('week : ', week)

        df = pd.DataFrame(week)
        # print(df)

        df[4] = df.groupby(by=[3])[0].transform(lambda x: x.cumsum())
        df[5] = df.groupby(by=[3])[1].transform(lambda x: x.cumsum())
        df[6] = df.groupby(by=[3])[2].transform(lambda x: x.cumsum())
        # print(df)
        # print(df.index.is_unique)
        # print(df[3][:])
        # print(df.groupby(level=0).last())
        ax = plt.subplot()

        ax.xaxis_date()

        BMJUA = fm.FontProperties(
            fname='/home/ubuntu/anaconda3/envs/python3/fonts/BMJUA_ttf.ttf')
        plt.title('영양분 변화', fontsize=30, fontproperties=BMJUA)

        w = 0.3
        idx = date2num(df[3])

        test1 = ax.bar(idx - w, df[4], width=w, color='g')
        test2 = ax.bar(idx, df[5], width=w, color='orange')
        test3 = ax.bar(idx + w, df[6], width=w, color='gold')
        ax.xaxis_date()
        plt.xticks(rotation=30)

        # for x in ax.patches:
        # height = x.get_height()
        # ax.text(x.get_x() + x.get_width()/2., height+3, height, ha='center', size=10)

        legend = ax.legend((test1, test2, test3),
                           ('Carbonhydrate', 'Protein', 'Fat'))
        frame = legend.get_frame()
        frame.set_alpha(1)
        frame.set_facecolor('none')  # legend

        img = BytesIO()
        plt.savefig(img, format='png', dpi=300)
        img.seek(0)
        return send_file(img, mimetype='image/png')


@ mainpage.route('/uploader')
class Register(Resource):
    def post(self):

        f = request.files['file']
        print('hi')

        f.save('../static/' + f.filename)

        return 'file uploaded successfully'


@ mainpage.route('/test')
class Register(Resource):
    def get(self):
        token = request.cookies.get('token')
        # 우리가 로그인에 성공한 경우 쿠키에 저장한 토큰을 가지고 옵니다

        session['token'] = token
        # flask 의 session 기능을 사용해서 token 이라는 key값에 token값을 저장해 줍니다
        # 앞으로 session에 token이라는 key의 존재 유무로 로그인 유무를 판단합니다

        return make_response(redirect('http://bp.aidetector.link/mainpage/'))
        # 사소한 작업을 마쳤다면 mainpage로 이동합니다


@ mainpage.route('/secret')
class Register(Resource):
    def get(self):
        return make_response(render_template('secret.html'))
