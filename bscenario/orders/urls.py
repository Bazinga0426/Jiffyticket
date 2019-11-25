from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('order/<int:order_id>/', views.order, name='detail'),
    path('order/cancel/<int:order_id>/', views.cancel, name='cancel'),
    path('order/complete/<int:order_id>/', views.complete, name='complete'),
    path('', views.list, name='list'),
]
