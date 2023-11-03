from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from .forms import MovieForm, GenreForm 

# Create your views here.
@require_safe
@require_http_methods(['GET'])
def index(request):
    movies = Movie.objects.all()
    # genres = Genre.objects.all()
    # print(genres)
    context = {
        'movies' : movies,
        # 'genres' : genres
    }
    return render(request, 'movies/index.html', context)


@require_safe
@require_http_methods(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # genre = movie.genres.all()
    

    context = {
        'movie' : movie,
        # 'genre' : genre,
    }
    return render(request, 'movies/detail.html', context)

@require_safe
def recommended(request):
    pass
