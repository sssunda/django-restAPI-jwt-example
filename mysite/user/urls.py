from .views import UserViewSet

user_list = UserViewSet.as_view({
    'get': 'list'
})
