from django.urls import path
from . import views
from register import views as rviews
from clubs import views as cviews
urlpatterns = [
    path('',views.detail,name='home_detail'),
    path('register/',rviews.register_student,name='register'),
    path('clubs/',cviews.clubs,name='clubs'),
    path('events/',views.events,name='events')
    ]
