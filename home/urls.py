from django.urls import path,include
from . import views
from clubs import views as cviews
urlpatterns = [
    path('',views.detail,name='home_detail'),
    path('clubs/',cviews.clubs,name='clubs'),
    path('events/',views.events,name='events'),
    path('placement/',include('placement.urls')),
    ]
