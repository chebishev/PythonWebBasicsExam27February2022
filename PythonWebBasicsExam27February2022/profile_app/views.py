from django.shortcuts import render, redirect

from PythonWebBasicsExam27February2022.album_app.models import Album
from PythonWebBasicsExam27February2022.profile_app.forms import ProfileForm
from PythonWebBasicsExam27February2022.profile_app.models import Profile


# Create your views here.
def home_page(request):
    profile = Profile.objects.first()
    if not profile:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home page')

        return render(request, 'home-no-profile.html', {'form': form})

    albums = Album.objects.all()
    return render(request, 'home-with-profile.html', {'albums': albums})


def profile_details(request):
    profile = Profile.objects.first()
    albums = 3
    return render(request, 'profile-details.html', {'profile': profile})


def profile_delete(request):
    return render(request, 'profile-delete.html')