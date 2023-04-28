from django.shortcuts import render
from movies.models import Movie
from shows.models import TVShow
from services import ScrapeMoviesService, ScrapeShowsService


def index(request):

    movie_service = ScrapeMoviesService()
    show_service = ScrapeShowsService()
    top_movies = movie_service.get_top_movies()
    top_shows = show_service.get_top_shows()
    # top_movies = []
    # top_shows = []
    for top_movie in top_movies:
        movie = (
            Movie.objects
            .filter(
                title=top_movie.get('title'),
                year=top_movie.get('year')
            )
            .first()
        )
        if movie:
            movie.poster_image = top_movie.get('poster_image')
            movie.rating = top_movie.get('rating')
            movie.save()
        else:
            movie = Movie(
                poster_image=top_movie.get('poster_image'),
                title=top_movie.get('title'),
                year=top_movie.get('year'),
                rating=top_movie.get('rating'),
            )
            movie.save()

    for top_show in top_shows:
        show = (
            TVShow.objects
            .filter(
                title=top_show.get('title'),
                year=top_show.get('year')
            )
            .first()
        )
        if show:
            show.poster_image = top_show.get('poster_image')
            show.rating = top_show.get('rating')
            show.save()
        else:
            show = TVShow(
                poster_image=top_show.get('poster_image'),
                title=top_show.get('title'),
                year=top_show.get('year'),
                rating=top_show.get('rating'),
            )
            show.save()

    return render(request, 'core/index.html')
