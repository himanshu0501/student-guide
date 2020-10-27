from django.urls import path
from . import views
from register import views as rviews

urlpatterns = [
    path('',views.detail,name='home_detail'),
    path('register/',rviews.register_student,name='register')

    ]
