from __future__ import unicode_literals
from time import timezone
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)




class Teacher(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    third_name = models.CharField(max_length=60, blank=True)
    faculty = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="email adres", max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    avatar = models.ImageField(blank=True, upload_to='static/img/avatar/')

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def save(self):
        self.set_password(self.password)
        super(Teacher, self).save()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
