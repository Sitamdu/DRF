# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse
#
# # Create your views here.
# def movie_list(request):
#     movie = Movie.objects.all()
#     data = {
#         # 'movies': movie.values()
#         'movies': list(movie.values())
#     }
#     return JsonResponse(data)
#
# def movie_detail(request,id):
#     movie = Movie.objects.get(id=id)
#     data = {
#         'movies': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     return JsonResponse(data)
