
from flask_restful import Resource
from modules.ArticlesResourceData import ArticlesResourceData

class ArticlesResource(Resource):
    def __init__(self):
        self.articleResourceDataObj = ArticlesResourceData()

    def get(self):
        return self.articleResourceDataObj.getArticles()