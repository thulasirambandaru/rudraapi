from flask import request
from flask_restful import Resource, reqparse, abort, Api
 
from . import app
 
api = Api(app, prefix='/myapi/v1')
 
def abort_if_song_doesnt_exist(song_name):
    if song_name not in SONGS:
        abort(404, message="Song {} doesn't exist".format(song_name))
 
parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('singer')
 
SONGS = {
'Song1': {
'title': 'Past Life',
'singer': 'Selena Gomez'
}
}
 
class Songs(Resource):
    def get(self):
        return {'songs': SONGS}
        
    def post(self):
        args = parser.parse_args(strict=True)
        song_name = int(max(SONGS.keys()).lstrip('Song')) + 1
        song_name = 'Song%d' % song_name
        SONGS[song_name] = {'title': args['title'], 'singer': args['singer']}
        return {
            song_name:SONGS[song_name]
        }, 201
 
    api.add_resource(Songs, '/songs')
 
class Song(Resource):
    def get(self, song_name):
        abort_if_song_doesnt_exist(song_name)
        return {
        song_name: SONGS[song_name]
    }
    
    def delete(self, song_name):
        abort_if_song_doesnt_exist(song_name)
        del SONGS[song_name]
        return '', 204
    
    def put(self, song_name):
        args = parser.parse_args(strict=True)
        abort_if_song_doesnt_exist(song_name)
        SONGS[song_name] = {'title': args['title'], 'singer': args['singer']}
        return {
            song_name: SONGS[song_name]
        }, 201
 
    api.add_resource(Song, '/songs/<string:song_name>')

