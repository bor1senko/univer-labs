from models import Teacher
from django.contrib.auth.hashers import check_password

class AuthBackend(object):
    def authenticate(self, email=None, password=None):
        try:
            user = Teacher.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except Teacher.DoesNotExist:
            return None


    def get_user(self, id=None):
        try:
            user = Teacher.objects.get(id=id)
            return user
        except Teacher.DoesNotExist:
            return None
