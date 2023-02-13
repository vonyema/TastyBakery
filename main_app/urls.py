from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('allproducts/',views.index, name='index'),
    path('allproducts/<int:bakedgood_id>/', views.bakedgood_detail, name='detail'),
    path('allproducts/<int:bakedgood_id>/add_detail/', views.add_order, name='add_'),
    path('add_order/', views.addItem, name='add_order'),
    path('cart/', views.shoppingcart, name="cart"),
    path('cart/<int:pk>/update/',views.EditCart.as_view(),name='editcart'),
    path('cart/<int:pk>/delete/',views.DeleteCart.as_view(),name='deletecart'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),

]