"""htwwg_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from htwwg import views as htwwg_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', htwwg_views.sighting_list),
    url(r'^admin/', admin.site.urls),
    url(r'^sighting/', include('htwwg.urls', namespace='htwwg')),
    url(r'^api/sighting/', include('htwwg.api.urls', namespace='api-sighting')),
    url(r'^user/', include('authentication.urls', namespace='user')),
    url(r'^api/user/', include('authentication.api.urls', namespace='api-user')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
