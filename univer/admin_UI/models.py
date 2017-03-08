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
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def save(self, update_fields=None):
        if self.pk is None:
            self.set_password(self.password)
        super(Teacher, self).save()


    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email + ' - ' + self.last_name + "  " + self.first_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Faculty(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField(max_length=150)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=60)
    teacher = models.ForeignKey(Teacher)
    groups = models.ManyToManyField('Group')

    def __unicode__(self):
        return "{0} - {1} {2}".format(self.name, self.teacher.first_name, self.teacher.last_name)

class Group(models.Model):
    name = models.CharField(max_length=20)
    specialty = models.ForeignKey(Specialty)

    def __unicode__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    third_name = models.CharField(max_length=60)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.last_name + ' ' + self.first_name

class Rating(models.Model):
    complid = models.BooleanField(default=False)
    value = models.IntegerField(blank=True, default=0)
    comment = models.TextField(blank=True)
    number_of_lab = models.IntegerField()
    subject = models.ForeignKey(Subject)
    student = models.ForeignKey(Student)

    def __unicode__(self):
        return '{0} - {1} {2}'.format(self.subject.name, self.student.last_name, self.student.first_name)
