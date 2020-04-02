from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('contactus/', views.contact_us, name='contact_us'),
    path('checkout/', views.checkout, name='checkout'),
    path('orderupdate/', views.orderupdate, name='orderupdate'),
    path('<int:myid>', views.prodview, name="ProductView"),
]
