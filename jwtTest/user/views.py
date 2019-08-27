from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser

User = get_user_model()

@authentication_classes((JSONWebTokenAuthentication,))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    lookup_field = 'username'

    def get_permissions(self):
        if self.action == 'create' :
            return (AllowAny(),)
        elif self.action == 'update' or self.action == 'destroy':
            return (IsLoggedInUserOrAdmin(),)
        elif self.action == 'list':
            return (IsAdminUser(),)
        return (IsLoggedInUserOrAdmin(),)

@permission_classes((IsAuthenticated,))
class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)