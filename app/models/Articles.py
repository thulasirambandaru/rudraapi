import datetime
from apiDB import db
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(1000))

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body
        }

    __mapper_args__ = {'primary_key':[id]}

    def __init__(self):
        pass