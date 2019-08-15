from rest_framework import serializers
from django.contrib.auth import get_user_model

# get_user_model helper함수를 통해 모델 클래스 참고
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    # def update(self, instance, validated_data):
    #     instance.email = validated_data['email']
    #     if validated_data['password'] != "":
    #         instance.set_password(validated_data['password'])
    #     instance.save()

    #     return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
