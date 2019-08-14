from rest_framework import serializers
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# get_user_model helper함수를 통해 모델 클래스 참고
# User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
