from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_summary, name='cart_summary'),
    path('add/', views.cart_add, name='create'),
    path('edit/<pk>', views.cart_edit, name='edit'),
    path('delete/<pk>', views.cart_delete, name='delete')
    ]