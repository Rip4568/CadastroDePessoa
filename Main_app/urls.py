from .views import HomeView
from django.urls import path
app_name = "Main_app"
urlpatterns = [
    path('',HomeView.as_view(),name='homeview'),
]
