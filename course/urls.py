from django.urls import path
from .views import *

app_name = 'course'

urlpatterns = [
    path('',Maincourse,name='courses'),
    path('category/<str:cat>',Maincourse,name='course_cat'),
    path('teacher/<str:teacher>',Maincourse,name='course_teacher'),
    path('search/',Maincourse,name='course_search'),
]