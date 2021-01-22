from django.urls import path,include
from placement import views
from user_profile import views as profile_views
from django.contrib.auth import views as auth_views # this is the views that django provide us inbuilt for user login and logout
# we will make the login page and logout page using these views given by django 
from django.conf import settings
from django.conf.urls.static import static  # these two import are needed when we are serving file
# we can serve uploaded media files from MEDIA_ROOT using the django.views.static.serve() but this is not good for production use.
# so if we are using the MEDIA_URL is defined as /media/ we can do this by using importing these things and then adding static into our urlpatterns





urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',profile_views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="placement/login.html"),name='login'), #here in as_view() we are providing the path to django where to look for the template 
    path('logout/',auth_views.LogoutView.as_view(template_name="placement/logout.html"),name='logout'), #here in as_view() we are providing the path to django where to look for the template
    # for logout by default django provide us but we can change that template as stated earlier.

]  


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
