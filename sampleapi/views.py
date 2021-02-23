from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import *
from .models import *



def home(request):
	return render(request, 'index.html')



#create Song
class SongView(generics.CreateAPIView):
	serializer_class = SongSerializers

	def get_queryset(self):
		# return Song.objects.filter(user=self.request.user, active=True)
		return Song.objects.all()

	def create(self, serializer):
		serializer = SongSerializers(data=self.request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#create Podcast
class PodcastView(generics.CreateAPIView):
	serializer_class = SongSerializers

	def get_queryset(self):
		return Podcast.objects.all()

	def create(self, serializer):
		serializer = PodcastSerializers(data=self.request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#create Audiobook
class AudiobookView(generics.CreateAPIView):
	serializer_class = AudiobookSerializers

	def get_queryset(self):
		return Audiobook.objects.all()

	def create(self, serializer):
		serializer = AudiobookSerializers(data=self.request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class SongDetailView(APIView):
#     #permission_classes = [IsAuthenticated]
  
#     def get_object(self):
#         try:
#             return Song.objects.all()
#         except Test.DoesNotExist:
#             raise Http404

#     def get(self):
#         try:
#             tests = self.get_object(request)
#             serializer = SongSerializers(tests)
#             return Response(serializer.data)
#         except Test.DoesNotExist as e:
#             return Response(status=status.HTTP_404_NOT_FOUND)
