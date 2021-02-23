from rest_framework import serializers	
from .models import Song, Podcast, Audiobook


class SongSerializers(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = '__all__'


class PodcastSerializers(serializers.ModelSerializer):
	class Meta:
		model = Podcast
		fields = '__all__'

class AudiobookSerializers(serializers.ModelSerializer):
	class Meta:
		model = Audiobook
		fields = '__all__'
