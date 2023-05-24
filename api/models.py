# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    descripton = models.TextField(blank=True, null=True)
    date_create = models.TextField(blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    cate = models.ForeignKey('Category', models.DO_NOTHING, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Album'
    def __str__(self):
        return self.id
    


class Artist(models.Model):
    id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    follow = models.IntegerField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    alias = models.TextField(primary_key=True)
    songs = models.ManyToManyField('Song', through='Artistsong', blank=True)
    albums = models.ManyToManyField(Album, through='Artistalbum', blank=True)
    class Meta:
        managed = False
        db_table = 'Artist'


class Artistalbum(models.Model):
    artist = models.ForeignKey(Artist, models.DO_NOTHING)
    album = models.ForeignKey(Album, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ArtistAlbum'


class Artistsong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING)
    artist = models.ForeignKey(Artist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ArtistSong'


class Category(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    songs = models.ManyToManyField('Song', through='Categorysong', related_name='categories', blank=True)
    class Meta:
        managed = False
        db_table = 'Category'



class Categorysong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING)
    cate = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CategorySong'


class Playlist(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    topic = models.ForeignKey('Topic', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    songs = models.ManyToManyField('Song', through='Playlistsong', blank=True)
    class Meta:
        managed = False
        db_table = 'Playlist'


class Playlistbyuser(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistByUser'


class Playlistbyusersong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING)
    playlist = models.ForeignKey(Playlistbyuser, models.DO_NOTHING)
    date_add = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistByUserSong'


class Playlistsong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING, blank=True, null=True)
    playlist = models.ForeignKey(Playlist, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistSong'


class Playlistuser(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    playlist_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistUser'


class Song(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    audio = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    album = models.ForeignKey(Album, models.DO_NOTHING, blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    listen = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    category = models.ManyToManyField(Category, through='Categorysong', blank=True)
    artists = models.ManyToManyField(Artist, through='Artistsong', blank=True)
    playlists = models.ManyToManyField(Playlist, through='Playlistsong', blank=True)
    class Meta:
        managed = False
        db_table = 'Song'
    def __str__(self):
        return self.id
    def is_favorite(self, user):
        if user.is_authenticated:
            usersong = Usersong.objects.filter(id_user=user, id_song=self).first()
            if usersong:
                return usersong.islike
        return False

class SongListenWeek(models.Model):
    song = models.ForeignKey(Song, models.DO_NOTHING, blank=True, null=True)
    listen = models.IntegerField(blank=True, null=True)
    date_listen  = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SongListenWeek'

class Topic(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    # playlist =models.OneToOneField(Playlist, models.DO_NOTHING, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Topic'


# class User(models.Model):
#     user_name = models.TextField(primary_key=True)
#     passwd = models.TextField()
#     name = models.TextField(blank=True, null=True)
#     email = models.TextField(blank=True, null=True)
#     thumbnail = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'User'





class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    thumbnail = models.TextField(blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
class Usersong(models.Model):
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user', to_field='username', blank=True, null=True)
    id_song = models.ForeignKey(Song, models.DO_NOTHING, db_column='id_song', blank=True, null=True)
    islike = models.BooleanField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    recenly_listen_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserSong'