from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('signin/', signin_view, name="signin"),
]
