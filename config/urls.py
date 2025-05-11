"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.attributes.urls')),
    path('api/', include('apps.banners.urls')),
    path('api/', include('apps.leave_requests.urls')),
    path('api/', include('apps.brands.urls')),
    path('api/', include('apps.catalogs.urls')),
    path('api/', include('apps.categories.urls')),
    path('api/', include('apps.commits.urls')),
    path('api/', include('apps.credits.urls')),
    path('api/', include('apps.delivery_methods.urls')),
    path('api/', include('apps.dashboard.urls')),
    path('api/', include('apps.desktops.urls')),
    path('api/', include('apps.desktops_fps.urls')),
    path('api/', include('apps.news.urls')),
    path('api/', include('apps.orders.urls')),
    path('api/', include('apps.payment_types.urls')),
    path('api/', include('apps.product_types.urls')),
    path('api/', include('apps.products.urls')),
    path('api/', include('apps.services.urls')),
    path('api/', include('apps.trade_in.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]

