from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path("detail/<int:mid>/", views.detail, name='detail')
]
