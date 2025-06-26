from django.urls import path
from . import views

'''urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # Additional paths for cart and checkout views
]

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),  # Cart page URL
    path('order_request/', views.order_request, name='order_request'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
]'''

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('update_cart/', views.update_cart, name='update_cart'),  # New route for updating cart
    path('order_request/', views.order_request, name='order_request'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
]
