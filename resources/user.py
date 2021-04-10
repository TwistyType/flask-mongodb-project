from flask import request, make_response
from database.models import User
from flask_jwt_extended import create_access_token
from flask_restful import Resource
import datetime


class UserRegister(Resource):
    def post(self):
        # add a user
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}

    def get(self):
        # see all registered users
        users = User.objects.to_json()
        resp = make_response(users)
        resp.headers['Accept'] = resp.headers['Content-Type'] = "application/json"
        return resp


class UserLogin(Resource):
    # login with userid and password
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password is incorrect'}, 401
        # access token expires in 2 days from creation
        expires = datetime.timedelta(days=2)
        access_token = create_access_token(
            identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
