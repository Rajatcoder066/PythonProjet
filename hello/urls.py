"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
admin.site.site_header="Rajat Ice-Cream Admin"
admin.site.site_title="Rajat Ice-Cream Portal"
admin.site.index_title="Rajat Ice-cream admin portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('home.urls')),
    path("about",include('home.urls')),
    path("services",include('home.urls')),
    path("contact",include('home.urls')),
    path("reg",include('home.urls')),
    path("login",include('home.urls')),
    path("data",include('home.urls')),
    path('product/<int:pk>/',include('home.urls')),
    path('product/<int:pk>/kart',include('home.urls')),
    path("product/<int:pk>/kart/order",include('home.urls')),
    path("product/<int:pk>/kart/order/contin",include('home.urls')),
    path("download",include('home.urls')),



    
    

]
