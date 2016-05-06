from pxl import models
from pxl import serializers
from rest_framework import generics, HTTP_HEADER_ENCODING, exceptions
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from django.utils.six import text_type
from django.utils.translation import ugettext_lazy as _
from rest_framework import parsers, renderers
from pxl.board_iot import generate_display
import base64
import binascii


def get_authorization_header(request):
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, text_type):
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth

def return_credentials(request):
    auth = get_authorization_header(request).split()

    if not auth or auth[0].lower() != b'basic':
        return None

    if len(auth) == 1:
        msg = _('Invalid basic header. No credentials provided.')
        raise exceptions.AuthenticationFailed(msg)
    elif len(auth) > 2:
        msg = _('Invalid basic header. Credentials string should not contain spaces.')
        raise exceptions.AuthenticationFailed(msg)
    try:
        auth_parts = base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(':')

    except (TypeError, UnicodeDecodeError, binascii.Error):
        msg = _('Invalid basic header. Credentials not correctly base64 encoded.')
        raise exceptions.AuthenticationFailed(msg)

    username, password = auth_parts[0], auth_parts[2]

    credentials = {
        'username': username,
        'password': password,
    }

    return credentials


class RegisterView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = serializers.UserSerializer1

    def post(self, request, *args, **kwargs):
        credentials = return_credentials(request)
        User.objects.create_user(**credentials)

        user = authenticate(**credentials)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class LoginView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = serializers.UserSerializer1

    def post(self, request, *args, **kwargs):
        credentials = return_credentials(request)

        user = authenticate(**credentials)
        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class BoardList(APIView):
    permission_classes = ()
    serializer_class = serializers.BoardSerializer

    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token'])
        user = User.objects.get(username=token.user.username)
        params = {}
        params['mlb'] = request.data['mlb']
        params['nfl'] = request.data['nfl']
        params['nhl'] = request.data['nhl']
        params['weather'] = request.data['weather']
        params['headlines'] = request.data['headlines']

        for key in params:
            if params[key]:
                params[key] = 'true'
            else:
                params[key] = ''
        try:
            board_instance = models.PXLBoardModel.objects.get(owner=user)
            board_instance.delete()
            board_instance = models.PXLBoardModel(
                owner=user,
                mlb=params['mlb'],
                nhl=params['nhl'],
                nfl=params['nfl'],
                headlines=params['headlines'],
                weather=params['weather'])
            board_instance.save()
            return Response({'token': token.key})
        except:
            newinstance = models.PXLBoardModel(
                owner=user,
                mlb=params['mlb'],
                nhl=params['nhl'],
                nfl=params['nfl'],
                headlines=params['headlines'],
                weather=params['weather'])
            newinstance.save()
            return Response({'token': token.key})
        finally:
            generate_display(params)
