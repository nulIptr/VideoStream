from flask import current_app
from . import db


class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    kind= db.Column(db.String(64))
    owner=db.Column(db.String(64))
    
    def __repr__(self):
        return '<Video %r>' % self.name