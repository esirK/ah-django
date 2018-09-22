# import jwt
#
# from django.conf import settings
#
# from rest_framework import authentication, exceptions
#
# from .models import User

"""Configure JWT Here"""
from rest_framework.authentication import BaseAuthentication, get_authorization_header


class JWTAuthentication(BaseAuthentication):
    # def authenticate(self, request):
    #     get_authorization_header
    #
    pass
