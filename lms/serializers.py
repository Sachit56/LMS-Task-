from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields="__all__"
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        fields="__all__"

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookDetailsModel
        fields="__all__"

class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowedBooksModel
        fields="__all__"        