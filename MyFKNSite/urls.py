"""MyFKNSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('shop.urls', namespace='shop')),
    path(r'^cart/', include('cart.urls', namespace='cart')),
    path(r'^', include('shop.urls', namespace='shop')),
    path(r'^order/', include('orders.urls', namespace='orders')),
    path(r'^paypal/', include('paypal.standard.ipn.urls')),
    path(r'^payment/', include('payment.urls', namespace='payment')),
    path(r'account/', include('user_shop.urls', namespace='user_shop')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
