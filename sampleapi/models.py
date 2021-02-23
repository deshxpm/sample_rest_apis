from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User



class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Song(ModelBase):
	# django created id by default
	song_name = models.CharField(max_length=100)
	duration_of_song = models.DurationField()
	uploaded_time = models.DateTimeField()

	def __str__(self):
		return self.song_name


class Podcast(ModelBase):
	# django created id by default
	podcast_name = models.CharField(max_length=100)
	duration_of_podcast  = models.DurationField()
	uploaded_time = models.DateTimeField()
	host = models.CharField(max_length=100)
	participants = models.CharField(max_length=100)


class Audiobook(ModelBase):
	# django created id by default
	audio_title = models.CharField(max_length=100)
	author_title = models.CharField(max_length=100)
	narrator = models.CharField(max_length=100)
	duration_of_audiobook = models.DurationField()
	uploaded_time = models.DateTimeField()