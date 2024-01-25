"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from lugares.views import base_test_view, landing_page_view,lugares_view,cities_view, add_local_view
from accounts.views import login_view,register_view, account_view,logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', landing_page_view, name = 'landing_page_view'),
    path('admin/', admin.site.urls),
    path('base/',base_test_view,name='base_test_view'),
    path('login/',login_view, name='login_view'),
    path('register/',register_view, name='register_view'),
    path('lugares/',lugares_view, name='lugares_view'),
    path('cities/',cities_view, name='cities_view'),
    path('account/', account_view,name='account_view'),
    path('logout/',logout_view,name='logout_view'),
    path('add_local/',add_local_view,name='add_local_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
