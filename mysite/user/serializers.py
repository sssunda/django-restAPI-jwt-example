from rest_framework import serializers
from django.contrib.auth import get_user_model

# get_user_model helper함수를 통해 모델 클래스 참고
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(required=False, write_only=True)
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, pk, validated_data):
        instance.email = validated_data['email']

        if validated_data.get('new_password') != None:
            instance.set_password(validated_data['new_password'])

        instance.save()

        return instance

    def destroy(self, instance):
        instance.delete()

    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'new_password' : {'write_only': True},
            'email':{'required':False},
        }
        fields = ('id', 'username', 'email', 'password', 'new_password')
