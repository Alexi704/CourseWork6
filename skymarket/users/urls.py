from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этого рекоммендуется использовать SimpleRouter

urlpatterns = [
]

users_router = SimpleRouter()
users_router.register("user", UserViewSet)

urlpatterns += users_router.urls
