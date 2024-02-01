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
from lugares.views import base_test_view, landing_pageView,cities_view, add_localView, lugaresView
from accounts.views import login_view,register_view, account_view,logout_view, user_locals_view, PasswordResetClass
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', landing_pageView.as_view(), name = 'landing_page_view'),
    path('admin/', admin.site.urls),
    path('base/',base_test_view,name='base_test_view'),
    path('login/',login_view, name='login_view'),
    path('register/',register_view, name='register_view'),
    path('lugares/',lugaresView.as_view(), name='lugares_view'),
    path('cities/',cities_view, name='cities_view'),
    path('account/', account_view,name='account_view'),
    path('logout/',logout_view,name='logout_view'),
    path('add_local/',add_localView.as_view(),name='add_local_view'),
    path('user_locals/',user_locals_view,name='user_locals_view'),
    path('reset_password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
