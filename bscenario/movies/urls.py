from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path("detail/<int:mid>/", views.detail, name='detail'),
    path("print-ticket/<int:order_id>/", views.print_ticket, name='print-ticket'),
    path('add-to-wish', views.add_to_wishlist, name='add-to-wishlist'),
    path('tops/', views.top_rank_movies, name='top-rank-movies'),
]
