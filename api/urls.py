from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path("api/albums", views.Category7List.as_view(), name=""),

    # path('api/topic/playlists',views.TopicListApiView.as_view()),
    path('api/albums',views.AlbumListApiView.as_view()),
    path('api/album/<str:id>',views.AlbumDetailApiView.as_view()),
    path('api/artists',views.ArtistListApiView.as_view()),
    path('api/playlists',views.TopicListApiView.as_view()),
    path('api/playlists/<str:id>',views.PlaylistDetailApiView.as_view()),
    path("api/playlist/<str:id>", views.PlaylistWithSongsDetailApiView.as_view(), name=""),
    path('api/songs',views.SongListApiView.as_view()),
    path('api/song/<str:id>',views.SongDetailApiView.as_view()),
    path('api/artist/<str:alias>',views.ArtistWithSongsApiView.as_view()),
    path('api/categories', views.CategoryListApiView.as_view()),
    path('api/category/<str:alias>',views.CategoryDetailApiView.as_view()),
    path('api/audio/<str:id>',views.AudioApiView, name="audio"),


    # user 
    path('api/register', views.UserRegisterApiView.as_view(), name='register'),
    path('api/login', views.UserLoginApiView.as_view(), name='login'),
    path('api/user', views.CurrentUserView.as_view(), name='user'),
    path('api/user/add-song-user', views.AddSongFavorite.as_view(), name='adduser'),
    path("api/user/playlist/<str:id>", views.PlaylistWithSongUserDetailApiView.as_view(), name=""),
    path("api/user/album/<str:id>", views.AlbumDetailUserApiView.as_view(), name=""),


    # search
    path('api/search/', views.SearchAPIView.as_view(), name='search'),

    #  recommend
    path('api/user/recommend/', views.SongRecommend.as_view(), name='recommend'),
    path('api/user/recommend/album', views.AlbumRecommend.as_view(), name='recommend'),
    
    # update luot nghe
    path('api/song/update-listen/<str:id>', views.UpdateSongListen.as_view(), name='update listen'),
    path('api/get-listen', views.GetSongListen.as_view(), name='get listen'), 
]
