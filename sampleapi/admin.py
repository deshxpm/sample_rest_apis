from django.contrib import admin

from .models import *



class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_name', 'duration_of_song', 'uploaded_time', 'added_date')



class PodcastAdmin(admin.ModelAdmin):
    list_display = ('id', 'podcast_name', 'duration_of_podcast', 'uploaded_time', 'host', 'participants', 'added_date')



class AudiobookAdmin(admin.ModelAdmin):
    list_display = ('id', 'audio_title', 'author_title', 'narrator', 'uploaded_time', 'duration_of_audiobook', 'added_date')        




admin.site.register(Song, SongAdmin)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Audiobook, AudiobookAdmin)