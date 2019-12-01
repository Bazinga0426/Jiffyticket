from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6a246fab5a70703ca261e8ccae458db63a17ccde
    path("detail/<int:mid>/", views.detail, name='detail'),
    path("print-ticket/<int:order_id>/", views.print_ticket, name='print-ticket'),
    path('add-to-wish', views.add_to_wishlist, name='add-to-wishlist'),
    path('tops/', views.top_rank_movies, name='top-rank-movies'),
<<<<<<< HEAD
=======
=======
    path("detail/<int:mid>/", views.detail, name='detail')
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705
>>>>>>> 6a246fab5a70703ca261e8ccae458db63a17ccde
]
