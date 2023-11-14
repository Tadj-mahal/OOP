from rest_framework import generics
from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Good, Token
from .serializers import GoodSerializer
from .classfile import TokenClass

class TokenAPIView(APIView):
    def get(self, request):
        token = TokenClass.create_token()
        return Response({'token': token})


class GoodAPIView(generics.ListCreateAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

    def get(self, request):
        token = request.GET['token']
        checker = TokenClass.check_token(token)
        if checker:
            return Response({'title': f'Error token was not registered'}, status=401)
        else:
            if Good.objects.all().count() > 0:
                return Response(Good.objects.all().values())
            else:
                return Response({'title': f'Token was created, but page empty'}, status=401)
        

    def post(self, request):
        post_new = Good.objects.create(
            name = request.data['name'],
            amount = request.data['amount'],
            price = request.data['price']
        )
        return Response({'post': model_to_dict(post_new)})