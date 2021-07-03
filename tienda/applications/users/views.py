# Third Party imports
from firebase_admin import auth

# Django imports
from django.shortcuts import render
from django.views.generic import TemplateView

# Django Rest imports
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Local imports
from .serializers import LoginSocialSerializer
from .models import User

# Create your views here.
class LoginUser(TemplateView):
    template_name = 'users/login.html'


class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        token_id = serializer.data.get('token_id')

        token_decoded = auth.verify_id_token(token_id)

        email = token_decoded['email']
        name = token_decoded['name']
        avater = token_decoded['picture']
        verified = token_decoded['email_verified']

        usuario, created = User.objects.get_or_create(
            email=email,
            defaults={
                'full_name': name,
                'email': email,
                'is_active': True
            }
        )
        if created:
            token = Token.objects.create(user=usuario)
        else:
            token = Token.objects.get(user=usuario)

        userGet = {
            'id': usuario.pk,
            'email': usuario.email,
            'full_name': usuario.full_name,
            'genero': usuario.genero,
            'date_birth': usuario.date_birth,
            'city': usuario.city
        }

        return Response(
            {
                'token': token.key,
                'user': userGet
            }
        )