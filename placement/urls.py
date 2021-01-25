from django.urls import path,include
from placement import views
from user_profile import views as profile_views
from django.contrib.auth import views as auth_views # this is the views that django provide us inbuilt for user login and logout
# we will make the login page and logout page using these views given by django 
from django.conf import settings
from django.conf.urls.static import static  # these two import are needed when we are serving file
# we can serve uploaded media files from MEDIA_ROOT using the django.views.static.serve() but this is not good for production use.
# so if we are using the MEDIA_URL is defined as /media/ we can do this by using importing these things and then adding static into our urlpatterns
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView# this is the class based view




urlpatterns = [
    path('',PostListView.as_view(),name='home'),  # first we have to change class based views to acutal views that can be done using as_views()
    path('post/<int:pk>/',PostDetailView.as_view(),name='blog'), # django provides to add variable in our route  pk is variable of type int this link will be used to see the individual post 
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='blog-update'), # we will update our post 
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='blog-delete'), 
    path('post/new/',PostCreateView.as_view(),name='blog-create'), # will be used to create the new post 
    path('profile/',profile_views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="placement/login.html"),name='login'), #here in as_view() we are providing the path to django where to look for the template 
    path('logout/',auth_views.LogoutView.as_view(template_name="placement/logout.html"),name='logout'), #here in as_view() we are providing the path to django where to look for the template
    # for logout by default django provide us but we can change that template as stated earlier.

]  


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
