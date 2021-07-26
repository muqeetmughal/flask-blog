from helpers.Base import BaseSchema
from models.Posts import Post


class PostSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Post
