from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

usermodel = get_user_model()


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = usermodel.objects.get(email=username)
        except usermodel.DoesNotExist:
            return None

        else:
            if user.check_password(password):
                return user
        return None
