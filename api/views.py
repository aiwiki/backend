from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .zingapi import ZingMp3Async
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.db.models import Count
from .models import *
from django.http import JsonResponse
from asgiref.sync import async_to_sync
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
class TopicListApiView(APIView):
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data, )
    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TopicDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Topic.objects.get(id=id)
        except Topic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        topic = self.get_object(id)
        serializer = TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        topic = self.get_object(id)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        topic = self.get_object(id)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistListApiView(APIView):
    def get(self, request):
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TopicPlaylistListApiView(APIView):
    def get(self, request, id):
        playlists = Playlist.objects.filter(topic=id)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PlaylistDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Playlist.objects.get(id=id)
        except Playlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        playlist = self.get_object(id)
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        playlist = self.get_object(id)
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        playlist = self.get_object(id)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistWithSongsDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Playlist.objects.get(id=id)
        except Playlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        user = request.user
        print(user)
        playlist = self.get_object(id)
        serializer = PlaylistWithSongsSerializer(playlist)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaylistWithSongUserDetailApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Playlist.objects.get(id=id)
        except Playlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        playlist = self.get_object(id)
        serializer = PlaylistWithSongsUserSerializer(playlist, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        playlist = self.get_object(id)
        serializer = PlaylistWithSongsUserSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumListApiView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AlbumDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Album.objects.get(id=id)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        album = self.get_object(id)
        serializer = AlbumSerializer(album)
        return Response(serializer.data, status=status.HTTP_200_OK)
class AlbumDetailUserApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Album.objects.get(id=id)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        album = self.get_object(id)
        serializer = Album4UserSerializer(album, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        album = self.get_object(id)
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        album = self.get_object(id)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ArtistListApiView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArtistDetailApiView(APIView):
    def get_object(self, alias):
        try:
            return Artist.objects.get(alias=alias)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, alias):
        artist = self.get_object(alias)
        serializer = ArtistWithSongsSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, alias):
        artist = self.get_object(alias)
        serializer = ArtistWithSongsSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, alias):
        artist = self.get_object(alias)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArtistWithSongsApiView(APIView):
    def get_object(self, alias):
        try:
            return Artist.objects.get(alias=alias)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, alias):
        artist = self.get_object(alias)
        songs = Song.objects.filter(artists=artist).order_by('-listen')[:10] # Lấy 10 bài hát có lượt nghe cao nhất của nghệ sĩ này
        serializer = ArtistWithSongsSerializer(artist)
        artist_data = serializer.data
        artist_data['songs'] = SongForArtistSerializer(songs, many=True).data # Chuyển đổi các bài hát thành dữ liệu được serialize
        return Response(artist_data, status=status.HTTP_200_OK)
    
    def put(self, request, alias):
        artist = self.get_object(alias)
        serializer = ArtistWithSongsSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SongListApiView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SongDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        song = self.get_object(id)
        serializer = SongForPlaylistSerializer(song)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response

    def put(self, request, id):
        song = self.get_object(id)        
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = self.get_object(id)
        song.delete()
        response = Response(status=status.HTTP_204_NO_CONTENT)
        return response

    
class CategoryListApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = CategoryListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailApiView(APIView):
    def get_object(self, alias):
        try:
            return Category.objects.get(alias=alias)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, alias):
        category = self.get_object(alias)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, alias):
        category = self.get_object(alias)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, alias):
        category = self.get_object(alias)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




async def getAudio(request, id):
    zi = ZingMp3Async()
    url = await zi.getAudio(id)
    data = {
        'url': url
    }
    return JsonResponse(data)

def AudioApiView(request, id):
    data = async_to_sync(getAudio)(request, id)
    return data

# user 
# import make_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
class UserRegisterApiView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            
            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }
                return Response(data, status=status.HTTP_200_OK)

            return Response({
                'error_message': 'Email or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class Category7List(APIView):
    def get(self, request, format=None):
        categories = Category.objects.annotate(num_albums=Count('album')).filter(num_albums__gte=7)
        serializer = CategoryAlbum7Serializer(categories, many=True)
        return Response(serializer.data)

class SearchAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('search', '')
        artist_qs = Artist.objects.filter(name__icontains=keyword).order_by('-follow')[:8] |\
            Artist.objects.filter(song__title__icontains=keyword)[:8]
        
        album_qs = Album.objects.filter(title__icontains=keyword).order_by('-like')[:9]
        playlist_qs = Playlist.objects.filter(title__icontains=keyword)[:9]
        song_qs = Song.objects.filter(title__icontains=keyword).order_by('-listen')[:8] | \
            Song.objects.filter(artist__name__icontains=keyword)[:8]
        artists_serializer = ArtistSerializer(artist_qs, many=True).data
        albums_serializer = AlbumSerializer(album_qs, many=True).data
        playlists_serializer = PlaylistSerializer(playlist_qs, many=True).data
        songs_serializer = SongForPlaylistSerializer(song_qs, many=True).data

        result = {
            'artists': artists_serializer,
            'albums': albums_serializer,
            'playlists': playlists_serializer,
            'songs': songs_serializer
        }

        serializer = SearchResultSerializer(data=result)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddSongFavorite(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        song_id = request.data.get('songId')
        islike = request.data.get('islike')
        try:
            user_song = Usersong.objects.get(id_user=user, id_song=song_id)
            serializer = UpdateUserSongSerializer(user_song, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=400)
        except Usersong.DoesNotExist:
            serializer = AddUserSongSerializer(data={
                'id_user': user,
                'id_song': song_id,
                'islike': islike,
            })
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=400)
    def post(self, request):
        user = request.user
        song_id = request.data.get('songId')
        islike = request.data.get('islike')
        duration  = request.data.get('duration')
        try:
            Usersong.objects.get(id_user=user, id_song=song_id)
            return Response({'error': 'UserSong already exists.'}, status=400)
        except Usersong.DoesNotExist:
            serializer = AddUserSongSerializer(data={
                'id_user': user,
                'id_song': song_id,
                'islike': islike,
                'duration': duration
            })
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=400)
from django.db.models.functions import Random
from django.db.models import Count, F, Value
class SongRecommend(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user.username
        song_ids = Song.objects.raw(f'''
            SELECT "Song".id
            FROM "Song"
            WHERE "Song".id IN (
                SELECT s.id
				from "Song" AS s
				JOIN "CategorySong" AS cs ON cs.song_id = s.id
				JOIN "Category" AS ct ON ct.id = cs.cate_id
				WHERE ct.title IN (SELECT ct.title
                                FROM "api_user" AS u
                                JOIN "UserSong" AS us ON u.username = us.id_user
                                JOIN "Song" AS s ON s.id = us.id_song
                                JOIN "CategorySong" AS cs ON cs.song_id = s.id
                                JOIN "Category" AS ct ON ct.id = cs.cate_id
                                where  u.username='{user}'
                                GROUP BY ct.title)
				Group by s.id
                order by random() limit 20) 
        ''')
        # lấy random 20 bài hát
        song_ids = Song.objects.filter(id__in=song_ids).order_by('?')[:20]
        # Sử dụng serializer để chuyển đổi kết quả thành JSON
        serializer = SongForPlaylistSerializer(song_ids, many=True)

        return Response(serializer.data)
class AlbumRecommend(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        user = request.user.username
        albums_ids = Album.objects.raw(f'''
                SELECT alb.id
				from "Album" AS alb
				JOIN "ArtistAlbum" AS ars ON ars.album_id = alb.id
				JOIN "Artist" AS ar ON ar.alias = ars.artist_id
				WHERE ar.name IN (SELECT ar.name
                                FROM "api_user" AS u
                                JOIN "UserSong" AS us ON u.username = us.id_user
                                JOIN "Song" AS s ON s.id = us.id_song
                                JOIN "ArtistSong" AS ars ON ars.song_id = s.id
								JOIN "Artist" AS ar ON ar.alias = ars.artist_id
                                where  u.username='hung'
                                GROUP BY ar.name)
				Group by alb.id
                order by random() limit 20
        ''')
        # lấy random 20 bài hát

        serializer = AlbumSerializer(albums_ids, many=True)
        return Response(serializer.data)
    
# update luot xem theo tuan trong thang
from datetime import datetime, timedelta, date
class GetSongListen(APIView):
    def get(self, request):
        
        songs = SongListenWeek.objects.filter(date_listen__gte=date.today() - timedelta(days=7)).order_by('-listen')[:10]
        serializer = SongListenWeekSerializer(songs, many=True)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateSongListen(APIView):

    def post(self, request, id):
        song =  Song.objects.get(id=id)
        date_now = date.today()
        
        song_in_week = SongListenWeek.objects.filter(song_id=id).order_by('-date_listen').first()
        if song_in_week:
            print(song_in_week)
            # nếu ngày trong tuần của bài hát đó trong tuần hiện tại thì cập nhật lại lượt nghe
            if song_in_week.date_listen > date_now - timedelta(days=7):
                song_in_week.listen += 1
                song_in_week.save()
                return Response({'success': 'Update success.'}, status=200)
            else:
                SongListenWeek.objects.create(song_id=song, date_listen=date_now, listen=1)
                return Response({'success': 'Create success.'}, status=200)
        else:
            SongListenWeek.objects.create(song_id=song, date_listen=date_now, listen=1)
            return Response({'error': 'SongListenWeek not exists.'}, status=200)

