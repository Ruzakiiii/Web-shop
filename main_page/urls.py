from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.abut),
    path('voyti',views.voyti),
    path('product/<str:pk>', views.get_product),
    path('products/<int:pk>', views.get_category),
    path('cart/<int:pk>', views.get_user_cart),
    path('cart/delete/<int:pk>', views.delete_item),
]