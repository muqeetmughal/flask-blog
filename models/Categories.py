from helpers.Base import BaseModel
from settings import db


class Category(BaseModel):
    __tablename__ = 'categories'
    name = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='category', lazy=True)

