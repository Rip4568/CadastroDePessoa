from .views import HomeView, RegisterView, RegisterView
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = "Main_app"
urlpatterns = [
    path('', HomeView.as_view(), name='homeview'),
    path('register/',RegisterView.as_view(),name='registerview'),
]