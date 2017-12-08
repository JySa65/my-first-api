from django.shortcuts import render
from rest_framework import viewsets
from account.serializers import UserSerializer
from account.models import Account
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer

    