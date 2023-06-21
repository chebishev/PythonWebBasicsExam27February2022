from django.shortcuts import render, redirect

from PythonWebBasicsExam27February2022.album_app.forms import CreateAlbumForm, EditAlbumForm
from PythonWebBasicsExam27February2022.album_app.models import Album
from PythonWebBasicsExam27February2022.profile_app.models import Profile


# Create your views here.
def album_add(request):
    form = CreateAlbumForm(request.POST or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.profile = Profile.objects.first()
        album.save()
        return redirect('home page')

    return render(request, 'add-album.html', {'form': form})


def album_details(request, id):
    album = Album.objects.get(id=id)
    return render(request, 'album-details.html', {'album': album})


def album_edit(request, id):
    album = Album.objects.get(id=id)
    form = EditAlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('home page')

    return render(request, 'edit-album.html', {'form': form, 'album': album})


def album_delete(request, id):
    album = Album.objects.get(id=id)
    return render(request, 'delete-album.html')
