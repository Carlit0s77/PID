"""djangocrud URL Configuration

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
from django.urls import path, include
from tareas import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', views.home, name='home'),
    path('arrendatarios/', views.arrendatarios, name='arrendatarios'),
    path('arrendatarios/create_arrendatario/',
         views.crear_arrendatario, name='crear_arrendatario'),
    path('arrendatarios/<int:arrendatario_id>/',
         views.arrendatario_datalle, name='arrendatario_detalle'),
    path('arrendatarios/<int:arrendatario_id>/delete/',
         views.delete_arrendatario, name='delete_arrendatario'),







]
