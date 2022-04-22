from matplotlib.font_manager import json_dump
from sqlalchemy.ext.declarative import DeclarativeMeta
from flask import request, jsonify, make_response
from flask_restx import Resource, Api, Namespace, fields
import json
from flask import redirect, url_for
from controll.user_account_model import UserTable
from controll.user_info_model import user_info_table
import datetime
import jwt


user_account = Namespace('user_account')

user_email_fields = user_account.model('email', {  # Model 객체 생성
    'user_email': fields.String(description='email', required=True)
})

user_pw_fields = user_account.inherit('User_email', user_email_fields, {
    'user_pw': fields.String(description='pw')
})

user_name_fields = user_account.inherit('User_pw', user_pw_fields, {
    'user_name': fields.String(description='name')
})


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):

        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    # this will fail on non-encodable values, like other classes
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


@user_account.route('/')
class UserAccount(Resource):
    @user_account.expect(user_pw_fields)
    @user_account.response(200, 'Success', user_pw_fields)
    def post(self):
        '''userid 체크 (로그인) true false tag id = user_id, user_pw'''
        user_email = request.json['user_email']
        user_pw = request.json['user_pw']
        # login.html로 부터 email 과 password를 전달받습니다

        result = UserTable.find_user(user_email, user_pw)
        # 전달받은 데이터를 통해 DB에 사용자가 있는지 없는지 검사합니다

        if result.json['status'] == True:
            token = jwt.encode({'user_email': user_email, 'exp':
                                datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},
                               'secret', algorithm='HS256')

            return jsonify({'massage': 'Success', 'status': True, 'token': token, 'user_email': user_email})
            # 해당 유저의 이메일이 존재하고 비밀번호 또한 일치한다면 token 을 생성한 뒤 login.html 로 자료들을 반환해줍니다
        else:
            return result
            # 실패했다면 그 이유를 그대로 반환해줍니다

    @user_account.expect(user_name_fields)
    @user_account.response(200, 'Success', user_name_fields)
    def put(self):
        '''userid 회원가입 true false tag id = user_id2, user_pw2'''
        user_email = request.json['user_email']
        user_name = request.json['user_name']
        user_pw = request.json['user_pw1']
        user_pw2 = request.json['user_pw2']
        # register.html 로부터 4가지의 정보를 받아옵니다
        if user_pw != user_pw2:
            return ({'massage': 'pw', 'status': False})
        # 우선적으로 2회에 걸쳐 입력된 비밀번호가 서로 일치하는지 확인합니다

        else:
            result = UserTable.add_user(user_email, user_name, user_pw)
            # UserTable 에서 유저 정보를 추가하는 함수를 호출합니다

            if result.json['status'] is True:
                return jsonify({'massage': 'Success', 'status': True})
                # 성공적으로 회원가입이 된 경우
            else:
                return result
                # 회원가입에 실패했다면 해당이유를 그대로 전달해줍니다
