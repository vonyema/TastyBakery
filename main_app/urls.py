from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('allproducts/',views.index, name='index'),
    path('allproducts/<int:bakedgood_id>/', views.bakedgood_detail, name='detail'),
    path('allproducts/<int:bakedgood_id>/add_detail/', views.add_order, name='add_'),
    path('cart/', views.shoppingcart, name="cart"),
]