from datetime import datetime
from flask import jsonify
from flask_restful import Resource, reqparse
from models.Articles import Articles

'''parserGet = reqparse.RequestParser()
parserGet.add_argument('title', type=str, required=False)
parserGet.add_argument('body', type=str, required=False) '''

class ArticlesResourceData(Resource):
    def getArticles(self):
        records = Articles.query.all()
        return jsonify([Articles.serialize(record) for record in records])