from django.shortcuts import render
from .models import TVShow


# Create your views here.
def top_shows(request):
    shows = TVShow.objects.all()

    context = {
        'shows': shows
    }
    return render(request, template_name='core/shows.html', context=context)
