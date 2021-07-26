from helpers.Base import BaseResource
from flask import request
from settings import db


class SingleUserResource(BaseResource):

    def get(self, id):
        from models.User import User
        from schemas.User import UserSchema
        user = User.query.filter_by(id=id).first()
        user_schema = UserSchema()
        # users_schema = UserSchema(many=True)

        return user_schema.dump(user)

    def post(self):
        from models.User import User
        from schemas.User import UserSchema
        # user = User.query.filter_by(id=id).first()
        json_output = request.get_json()
        user_schema = UserSchema()

        new_user = user_schema.load(json_output)

        user = User(**new_user)

        user.save()

        return user_schema.dump(user)



class UserListResource(BaseResource):

    def get(self, id):
        from models.User import User
        from schemas.User import UserSchema
        user = User.query.filter_by(id=id).first()
        user_schema = UserSchema()
        # users_schema = UserSchema(many=True)

        return user_schema.dump(user)

    def post(self):
        from models.User import User
        from schemas.User import UserSchema
        # user = User.query.filter_by(id=id).first()
        json_output = request.get_json()
        user_schema = UserSchema()

        new_user = user_schema.load(json_output)

        user = User(**new_user)

        user.save()

        return user_schema.dump(user)