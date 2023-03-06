from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

user_router = SimpleRouter()
user_router.register("users", UserViewSet, basename='users')

urlpatterns = [
    #path("", include("user_router.urls")),
    path("", include("djoser.urls")),
    path("token/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
