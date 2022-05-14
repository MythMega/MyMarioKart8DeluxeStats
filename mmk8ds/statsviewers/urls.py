from django.urls import path
from . import views

app_name = "statsviewers"

urlpatterns = [
    path('', views.index, name='index'),
    path('tracks/', views.tracks, name='tracks'),
    path('builds/', views.builds, name='builds'),
]