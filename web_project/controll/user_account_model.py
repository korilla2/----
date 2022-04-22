from marshmallow import Schema, fields, validate
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import bcrypt


user_account_db = SQLAlchemy()


class UserTable(user_account_db.Model):
    __tablename__ = 'user_account'

    ID = user_account_db.Column(
        user_account_db.Integer, primary_key=True, autoincrement=True)
    Email = user_account_db.Column(
        user_account_db.String(1000, 'utf8mb4_unicode_ci'))
    name = user_account_db.Column(
        user_account_db.String(1000, 'utf8mb4_unicode_ci'))
    pw = user_account_db.Column(
        user_account_db.String(1000, 'utf8mb4_unicode_ci'))

    def __init__(self, Email, name, pw):
        self.Email = Email
        self.name = name
        self.pw = pw

    # 유저 추가
    def add_user(email, name, pw):
        hash_pw = bcrypt.hashpw(
            pw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        # 비밀번호를 bcrypt를 사용해서 암호화합니다
        # encode 까지만 실행시키면 binary값으로 존재합니다
        # 이 때 binary 값이 아닌 string값으로 DB에 저장시키기 위해서
        # decode를 한 번 해준 상태입니다

        user = UserTable.find_user(email, pw)
        # 일단 겹치는 유저가 있는지 먼저 찾습니다

        if (user.json['status'] == False) & (user.json['massage'] == 'email'):
            user = UserTable(email, name, hash_pw)
            user_account_db.session.add(user)
            user_account_db.session.commit()
            return jsonify({'massage': 'Success', 'status': True})
            # 겹치는 유저가 없다면 DB에 해당 정보들을 저장하고 반영합니다
            # 그 뒤 자료를 user_account - put 으로 반환합니다
        else:
            return jsonify({'massage': 'ID', 'status': False})
            # 실패한 경우는 이미 해당 email이 존재하는 경우입니다

    # 유저 조회
    def find_user(email, pw):
        user = UserTable.query.filter((UserTable.Email == email)).first()
        # user_account 에서 보낸 email 을 토대로 해당 유저가 존재하는지 확인합니다

        if user is None:
            return jsonify({'massage': 'email', 'status': False})
        # 유저가 존재하지 않는경우

        else:
            db_pw = user.pw
            result = bcrypt.checkpw(pw.encode(
                'utf-8'), db_pw.encode('utf-8'))
            # 유저가 존재한다면 DB에 저장된 password와 받아온 password를 비교합니다
            # 암호화 되어서 저장되어 있기 때문에 bcrypt의 checkpw 함수를 이용합니다

            if result == True:
                return jsonify({'massage': 'Success', 'status': True})
            # 로그인이 된 경우

            else:
                return jsonify({'massage': 'PW', 'status': False})
            # 비밀번호가 달라서 실패한 경우


# class UsersSchema(MA.Schema):
#     not_blank = validate.Length(min=1, error='Field cannot be blank')
#     id = fields.Integer(dump_only=True)
#     user_id = fields.String(validate=not_blank)
#     user_pw = fields.String(validate=not_blank)
