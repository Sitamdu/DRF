from django.urls import path
from home.API.views import StreamAV,WatchListAV,WatchDetailAV,StreamDetailAV,ReviewList,ReviewDetail


urlpatterns = [
    # path('list/', movie_list, name ='movie-list'),
    # path('detail/<int:id>/', movie_detail, name = 'movie-detail'),

    path('list/', WatchListAV.as_view(), name='Watch-list'),
    path('detail/<int:id>', WatchDetailAV.as_view(), name='movie-detail'),

    path('stream/', StreamAV.as_view(),name='stream'),
    path('stream/<int:id>', StreamDetailAV.as_view(), name='stream-detail'),

    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

]
