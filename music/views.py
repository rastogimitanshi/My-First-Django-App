from django.http import HttpResponse
from .models import Album
from django.http import Http404
from django.shortcuts import render
from django.template import loader
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums,}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Oops Album Does not Exist!")
    return render(request, 'music/detail.html', {'album' : album})
