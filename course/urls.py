from django.urls import path
from .views import *

app_name = 'course'

urlpatterns = [
    path("",courses,name="courses"),
]