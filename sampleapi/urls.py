from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.home, name='homepage'),
    path('api_register/song/post/', views.SongView.as_view(), name='Song'),
    # path('api_register/get/', views.SongDetailView.as_view(), name='SongDetailView'),
    path('api_register/podcast/post/', views.PodcastView.as_view(), name='Podcast'),
    path('api_register/audiobook/post/', views.AudiobookView.as_view(), name='Audiobook'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
