from helpers.Base import BaseSchema
from models.User import User


class UserSchema(BaseSchema):
    from marshmallow import fields
    from schemas.Post import PostSchema

    class Meta(BaseSchema.Meta):
        model = User
        load_only = ('password',)
        dump_only = ('id',)

    posts = fields.Nested(PostSchema)
