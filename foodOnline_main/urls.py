"""foodOnline_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
from foodOnline_main.apps.marketplace import views as MarketplaceViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account/', include('foodOnline_main.apps.accounts.urls')),
   
    #For Business Restaurant Owner
    path('vendor/', include('foodOnline_main.apps.vendor.urls')),
    
    #For Customer 
    path('customer/', include('foodOnline_main.apps.customers.urls')),
    
    #MarketPlace with Cart Products
    path('marketplace/', include('foodOnline_main.apps.marketplace.urls')),
    path('cart/', MarketplaceViews.cart, name='cart'),
    path('search/', MarketplaceViews.search, name='search'),
    
    path('checkout/', MarketplaceViews.checkout, name='checkout'),

    # ORDERING- Placing order, payment and order success.
    path('orders/', include('foodOnline_main.apps.orders.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
