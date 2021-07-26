from helpers.Base import BaseModel
from settings import db


class Post(BaseModel):
    __tablename__ = 'posts'
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),
                            nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=False)
