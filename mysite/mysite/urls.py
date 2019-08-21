from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/login/', obtain_jwt_token),
    path('api/auth/me/', views.UserRetrieveAPIView.as_view()),
    path('api/auth/refresh/', refresh_jwt_token),
]