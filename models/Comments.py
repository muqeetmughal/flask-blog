from helpers.Base import BaseModel
from settings import db
import datetime


class Comment(BaseModel):
    __tablename__ = 'comments'
    title = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
