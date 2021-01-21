from django.urls import path,include
from placement import views
from django.contrib.auth import views as auth_views # this is the views that django provide us inbuilt for user login and logout
# we will make the login page and logout page using these views given by django 




urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="placement/login.html"),name='login'), #here in as_view() we are providing the path to django where to look for the template 
    path('logout/',auth_views.LogoutView.as_view(template_name="placement/logout.html"),name='logout'), #here in as_view() we are providing the path to django where to look for the template
    # for logout by default django provide us but we can change that template as stated earlier.

]  