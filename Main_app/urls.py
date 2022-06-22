from .views import HomeView
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = "Main_app"
urlpatterns = [
    path('', login_required(HomeView.as_view()), name='homeview'),

]
