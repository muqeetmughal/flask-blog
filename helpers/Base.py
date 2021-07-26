from flask_restful import Resource
from settings import ma, db
import datetime


class BaseResource(Resource):
    pass


class BaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        include_fk = True


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    # created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(datetime.timezone.utc))
    # updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def before_save(self, *args, **kwargs):
        pass

    def after_save(self, *args, **kwargs):
        pass

    def save(self, commit=True):
        self.before_save()
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

        self.after_save()

    def before_update(self, *args, **kwargs):
        pass

    def after_update(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        self.before_update(*args, **kwargs)
        db.session.commit()
        self.after_update(*args, **kwargs)

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()
