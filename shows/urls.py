from django.urls import path
from .views import top_shows


urlpatterns = [
    path('shows/', top_shows, name='shows')
]
