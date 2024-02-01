from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

class UserView(APIView):

    def get(self,request):
        users=UserModel.objects.all()
        serializer=UserSerializer(users,many=True)

        return Response({'status':200,'users':serializer.data})






