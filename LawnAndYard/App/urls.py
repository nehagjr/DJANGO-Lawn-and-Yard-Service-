from django.urls import path
from .views import *
urlpatterns = [
   path('',index, name='index'),
   path('login/',login,name='login'),
   path("dashboard/",registerdata,name='dashboard'),

]