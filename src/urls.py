"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from src import views
from src import backend_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),  # Ensure this line exists
    path('', views.home, name='home'),
    path('record-sale/', views.record_sale, name='record_sale'),
    path('set-pricing/', views.set_pricing, name='set_pricing'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('view-sales/', backend_views.view_sales, name='view_sales'),
    path('transfer-money/', backend_views.transfer_money, name='transfer_money')
]

