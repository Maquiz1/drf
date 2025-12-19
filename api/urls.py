from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('product-info/', views.product_info, name='product-info'),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list'),
    path('user-orders/', views.UserOrderListAPIView.as_view(), name='user-order-list'),
]