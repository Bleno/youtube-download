from pyramid.view import view_config
from pyramid.response import Response
import youtube_dl
import uuid
import os
import urllib


@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view(request):
    videos = [ f  for f in os.listdir('/tmp') if f.endswith('.mp4') or f.endswith('.webm')]
    videos = [(video ,urllib.parse.quote(video),) for video in videos ]
    return {'project': 'youtube', 'videos': videos }



@view_config(route_name='youtube-dl', renderer='json', request_method=['POST'])
def get_youtube(request):
    url = request.params['url']
    out_dir = '/tmp'
    name = uuid.uuid4().hex
    print(name)
    #name = 'git'
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%s/%%(title)s.%%(ext)s' % out_dir})
    y = ydl.extract_info(url) # aqui colocar a url
    name = y['title']
    return [ f  for f in os.listdir('/tmp') if f.startswith(name)]


@view_config(route_name='download')
def download(request):
    name = request.matchdict['name']
    _file = open('/tmp/' + name, 'rb')
    return Response(_file.read(), content_type="application/octet-stream")


@view_config(route_name='delete-file', renderer='json', request_method=['POST'])
def delete_file(request):
    name = request.params['name']
    try:
        os.remove("/tmp/" + name)
        print("removendo video")
        return {'result': True, 'message': 'Arquivo removido'}
    except Exception as e:
        print(str(e))
        print("Erro ao remover video")
        return {'result': False, 'message': 'Não foi possível remover arquivo'}
