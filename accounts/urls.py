from django.urls import path
from .views import UserCreateView,UserLoginView


app_name="accounts"

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    path('signup',UserCreateView.as_view(),name='signup'),
]
