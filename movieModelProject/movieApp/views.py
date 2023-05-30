from django.shortcuts import render
from movieApp.models import Movie
from movieApp.forms import MovieForm

# Create your views here.
def index(request):
    return render(request,'movieApp/index.html')

def listMovies(request):
    movies_list = Movie.objects.all()
    return render(request, 'movieApp/listMovies.html', {'movies':movies_list})

def addMovie(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)    
    return render(request, 'movieApp/addMovie.html', {'form':form})
