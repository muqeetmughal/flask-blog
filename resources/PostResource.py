from helpers.Base import BaseResource
from flask import request
from settings import db


class SinglePostResource(BaseResource):

    def get(self, id):
        from models.Posts import Post
        from schemas.Post import PostSchema
        post = Post.query.filter_by(id=id).first()
        post_schema = PostSchema()
        # users_schema = UserSchema(many=True)

        return post_schema.dump(post)

    def post(self):
        from models.Posts import Post
        from schemas.Post import PostSchema
        # user = User.query.filter_by(id=id).first()
        json_output = request.get_json()
        post_schema = PostSchema()

        new_post = post_schema.load(json_output)

        post = Post(**new_post)

        post.save()

        return post_schema.dump(post)
