#-*- coding:utf-8 -*-
from Base.models import RangoUser
from django.conf import settings
import re


class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if re.match(r"[^@]+@[^@]+\.[^@]+", username):
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = RangoUser.objects.get(**kwargs)
            print(user.is_authenticated())
            if user.check_password(password):
                return user
        except RangoUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return RangoUser.objects.get(pk=user_id)
        except RangoUser.DoesNotExist:
            return None
