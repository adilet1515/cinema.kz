from django.urls import path
from .views import CreateUserView,LoginUserView,LogoutUserView
app_name = 'users'

urlpatterns = [
    path("create/", CreateUserView.as_view() , name="register"),
    path("login/", LoginUserView.as_view() , name="login"),
    path("logout/", LogoutUserView.as_view() , name="logout"),
]