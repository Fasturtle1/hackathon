from hashlib import sha256

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, _user_has_perm, UserManager
from django.db import models
from django.utils.crypto import get_random_string, constant_time_compare


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField('Логин', max_length=64, unique=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    patronym = models.CharField('Отчество', max_length=50, null=True, blank=True)
    email = models.CharField('Электронная почта', max_length=64, null=True, default=None, blank=True)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'login'
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def set_password(self, raw_password):
        salt = get_random_string(64)
        hasher = sha256()
        raw_password = raw_password + '_' + salt
        hasher.update(raw_password.encode('utf-8'))
        self.salt = salt
        self.password = hasher.hexdigest()
        return self

    def check_password(self, raw_password):
        hasher = sha256()
        raw_password = raw_password + '_' + self.salt
        hasher.update(raw_password.encode('utf-8'))
        result = constant_time_compare(hasher.hexdigest(), self.password)
        return result

    def has_perm(self, perm, obj=None):
        # Не уволенные суперпользователи имеют весь доступ
        if not self.is_active and self.is_superuser:
            return True
        return _user_has_perm(self, perm, obj)

    @property
    def is_staff(self):
        return self.is_superuser
