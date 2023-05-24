from rest_framework import serializers
from .models import *
from django.db.models import Count

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ArtistsongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artistsong
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistbyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlistbyuser
        fields = '__all__'

class PlaylistbyusersongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlistbyusersong
        fields = '__all__'

class PlaylistsongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlistsong
        fields = '__all__'

class PlaylistuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlistuser
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class Cate4AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title','alias']
class ArtistForSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name','alias']
class SongForPlaylistUserSerializer(serializers.ModelSerializer):
    artists = ArtistForSongSerializer(many=True)
    islike = serializers.SerializerMethodField()
    class Meta:
        model = Song
        fields = ['id','title', 'artists','thumbnail', 'album', 'audio','duration','listen','islike'] 
    def get_islike(self, obj):
        user = self.context.get('user')
        if Usersong.objects.filter(id_user=user, id_song=obj).exists():
            usersong = Usersong.objects.get(id_user=user, id_song=obj)
            return usersong.islike
        return False

class Album4UserSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()
    def get_songs(self, obj):
        user = self.context.get('user')
        song = Song.objects.filter(album=obj)
        serializer = SongForPlaylistUserSerializer(song,context={'user': user}, many=True)
        return serializer.data
    class Meta:
        model = Album
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()
    def get_songs(self, obj):
        song = Song.objects.filter(album=obj)
        serializer = SongForPlaylistSerializer(song, many=True)
        return serializer.data
    class Meta:
        model = Album
        fields = '__all__'
class SongForPlaylistSerializer(serializers.ModelSerializer):
    artists = ArtistForSongSerializer(many=True)
    class Meta:
        model = Song
        fields = ['id', 'title', 'artists','thumbnail', 'album', 'audio','duration','listen']
class PlaylistWithSongsSerializer(serializers.ModelSerializer):
    songs = SongForPlaylistSerializer(many=True)
    class Meta:
        model = Playlist
        fields = '__all__'

class UserRecommendSerializer(serializers.ModelSerializer):
    songs = SongForPlaylistSerializer(many=True)
    

class PlaylistWithSongsUserSerializer(serializers.ModelSerializer):
    songs = SongForPlaylistUserSerializer(many=True)
    class Meta:
        model = Playlist
        fields = '__all__'
class AlbumsWithSongsSerializer(serializers.ModelSerializer):
    songs = SongForPlaylistSerializer(many=True)
    class Meta:
        model = Album
        fields = '__all__'
class SongForArtistSerializer(serializers.ModelSerializer):
    artists = ArtistForSongSerializer(many=True)
    class Meta:
        model = Song
        fields = ['id', 'title', 'artists','thumbnail', 'album', 'audio','duration','listen']
class Album4ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'thumbnail']
class ArtistWithSongsSerializer(serializers.ModelSerializer):
    songs = SongForArtistSerializer(many=True)
    albums = Album4ArtistSerializer(many=True)
    class Meta:
        model = Artist
        fields = '__all__'
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','alias']
class PlaylistWithoutSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id','title','thumbnail','description']
class TopicSerializer(serializers.ModelSerializer):
    playlists = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = '__all__'

    def get_playlists(self, obj):
        playlists = Playlist.objects.filter(topic=obj)
        serializer = PlaylistWithoutSongsSerializer(playlists, many=True)
        return serializer.data

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password': {'write_only': True}}
        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
            return user
class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategoryAlbumCountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    num_albums = serializers.IntegerField()

class Album4CateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'thumbnail']


class CategoryAlbum7Serializer(serializers.ModelSerializer):
    num_albums = serializers.SerializerMethodField()
    albums = serializers.SerializerMethodField()

    def get_num_albums(self, obj):
        return obj.album_set.count()

    def get_albums(self, obj):
        albums = obj.album_set.annotate(num_songs=Count('song')).order_by('-num_songs')[:14]
        return Album4CateSerializer(albums, many=True).data


    class Meta:
        model = Category
        fields = ('id', 'title', 'num_albums', 'albums')



class SearchResultSerializer(serializers.Serializer):
    artists = ArtistSerializer(many=True)
    albums = AlbumSerializer(many=True)
    playlists = PlaylistSerializer(many=True)
    songs = SongForPlaylistSerializer(many=True)



class UserSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersong
        fields = '__all__'
class UserSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersong
        fields = '__all__'


class UpdateUserSongSerializer(serializers.ModelSerializer):
    islike = serializers.BooleanField(required=True)

    class Meta:
        model = Usersong
        fields = ['islike']

    def update(self, instance, validated_data):
        instance.islike = validated_data['islike']
        instance.save()
        return instance
class AddUserSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersong
        fields = ['id_user', 'id_song','islike']

    def create(self, validated_data):
        id_user = validated_data.get('id_user')
        song_id = validated_data.get('id_song')
        islike = validated_data.get('islike') if validated_data.get('islike') else False
        duration = validated_data.get('duration') if validated_data.get('duration') else 0
        user_song = Usersong.objects.create(
            id_user=id_user,
            id_song=song_id,
            islike= islike,
            duration=duration
        )
        return user_song
class Song4ListenWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'artists']

class SongListenWeekSerializer(serializers.ModelSerializer):
    # get name song
    song = serializers.SerializerMethodField()
    def get_song(self, obj):
        song = Song.objects.get(id=obj.song_id)
        serializer = Song4ListenWeekSerializer(song)
        return serializer.data
    class Meta:
        model = SongListenWeek
        fields = ['listen', 'song']