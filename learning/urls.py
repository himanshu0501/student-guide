"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static  # these two import are needed when we are serving file
# we can serve uploaded media files from MEDIA_ROOT using the django.views.static.serve() but this is not good for production use.
# so if we are using the MEDIA_URL is defined as /media/ we can do this by using importing these things and then adding static into our urlpatterns



urlpatterns = [
    path('home/',include('home.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
