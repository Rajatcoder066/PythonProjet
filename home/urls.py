from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index,name='home'),
    path("about", views.about,name='about'),
    path("services", views.services,name='services'),
    path("contact", views.contact,name='contact'),
    path("reg",views.reg,name='reg'),
    path("login",views.login,name='login'),  
    path("data",views.data,name='data'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/kart', views.kart, name='kart'),
    path("product/<int:pk>/kart/order",views.order,name='order'),
    path("product/<int:pk>/kart/order/contin",views.contin,name='contin'),
    path('download', views.download, name='download')
]
 