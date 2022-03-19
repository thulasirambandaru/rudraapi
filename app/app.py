import datetime
from distutils.log import debug
from posixpath import supports_unicode_filenames
from unittest import result
from flask import Flask, jsonify, request
from flask_restful import Resource, reqparse, abort, Api
#from flask_marshmallow import Marshmallow
from flask_cors import CORS
from apiDB import app, db
from controllers.ArticlesResource import ArticlesResource
from controllers.ManufactureOrders import ManufactureOrders, ManufactureOrderItems


api = Api(app, prefix='/api/v1')
CORS(app)

#ma = Marshmallow(app)


'''
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('title', type=str, required=True, help="odometer is required parameter!")
parser.add_argument('body', type=str, required=True, help="fuelQuantity is required parameter!")
'''

'''class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'created')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)'''




'''class ArticleOperations(Resource):
    def get(self):
        records = Articles.query.all()
        return jsonify([Articles.serialize(record) for record in records])
        

    @app.route('/get/<id>/', methods = ['GET'])
    def get_article(id):
        article = Articles.query.get(id)
        return article_schema.jsonify(article)

    @app.route('/add/', methods = ['POST'])
    def add_article():
        title = request.json['title']
        body = request.json['body']

        articles = Articles(title, body)
        db.session.add(articles)
        db.session.commit()
        return article_schema.jsonify(articles)

    @app.route('/update/<id>/', methods = ['PUT'])
    def update_article(id):
        article = Articles.query.get(id)

        title = request.json['title']
        body = request.json['body']

        article.title = title
        article.body = body

        db.session.commit()
        return article_schema.jsonify(article)

    @app.route('/delete/<id>/', methods = ['DELETE'])
    def delete_article(id):
        article = Articles.query.get(id)
        db.session.delete(article)
        db.session.commit()
        return article_schema.jsonify(article) '''


api.add_resource(ArticlesResource, '/articles')
api.add_resource(ManufactureOrders, '/morders')
api.add_resource(ManufactureOrderItems, '/morders/<int:orderID>')

if __name__ == "__main__":
    app.run(debug=True)