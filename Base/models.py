from Base import modelsConfig as mC, modelsFunctions as fM, userManager as uM
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField


# Create your models here.
class RangoUser(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=mC.RangoUser_NicknameLength, blank=True, null=True,
                                verbose_name='Nickname')
    fullname = models.CharField(max_length=mC.RangoUser_FullnameLength, blank=True, null=True,
                                verbose_name='Fullname')
    avatar = ThumbnailerImageField(upload_to=fM.avatarFile, default=mC.RangoUser_AvatarDefault, blank=True, null=True,
                                   verbose_name='Avatar')
    username = models.CharField(max_length=mC.RangoUser_UsernameLength, blank=False, null=False, unique=True,
                                verbose_name='Username (For login)')
    email = models.EmailField(blank=False, null=False, unique=False,
                              verbose_name='Email (For login)')
    birthday = models.DateField(blank=True, null=True,
                                verbose_name='Birthday')
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = uM.UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        name = self.nickname if self.nickname != '' else self.username
        return "%s" % name

    def get_fullname(self):
        return "%s" % self.fullname

    def get_full_name(self):
        return self.get_fullname()

    def get_username(self):
        return "%s" % self.username

    def get_nickname(self):
        return "%s" % self.nickname

    def get_short_name(self):
        return self.get_nickname()

    def is_authorized(self):
        return self.is_active

    def is_admin(self):
        return self.is_staff

    def is_super(self):
        return self.is_superuser