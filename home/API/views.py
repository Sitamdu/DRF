from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics

from home.models import Streaming,WatchList,Reviews
from .serializers import WatchlistSerializer,StreamSerializer,ReviewSerializer



#concrete CBV
class ReviewList(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


# class ReviewDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


#CBV
class WatchListAV(APIView):

    def get(self,request):
        movies = WatchList.objects.all()
        serializer = WatchlistSerializer(movies,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):

    def get(self,request,id):
        try:
            movies = WatchList.objects.get(id=id)
        except WatchList.DoesnotExist:
            return Response({'error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchlistSerializer(movies)
        return Response(serializer.data)

    def put(self,request,id):
        movies = WatchList.objects.get(id=id)
        serializer = WatchlistSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        movies = WatchList.objects.get(id=id)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamAV(APIView):

    def get(self,request):
        platform = Streaming.objects.all()
        serializer = StreamSerializer(platform, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = StreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamDetailAV(APIView):

    def get(self,request,id):
        try:
            stream = Streaming.objects.get(id=id)
        except Streaming.Doesnotexist:
            return Response({'error': 'details not found'}, status= status.HTTP_400_BAD_REQUEST)

        serializer = StreamSerializer(stream)
        return Response(serializer.data)

    def put(self,request,id):
        stream = Streaming.objects.get(id=id)
        serializer = StreamSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        remove = Streaming.objects.get(id=id)
        remove.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#FBV
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,id):
#
#     if request.method =='GET':
#
#         try:
#             movies = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response({'error':'movie not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = MovieSerializer(movies)
#         return Response(serializer.data)
#
#     if request.method =='PUT':
#         movies = Movie.objects.get(id=id)
#         serializer = MovieSerializer(movies, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     if request.method =='DELETE':
#         movies = Movie.objects.get(id=id)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


