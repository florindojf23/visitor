from django.urls import path
from .views import *

urlpatterns = [
	path('',userlist,name="userlist"),
]