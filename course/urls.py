from django.urls import path
from .views import *

app_name = 'course'

urlpatterns = [
    path('',Maincourse,name='courses'),
    path('category/<str:cat>',Maincourse,name='course_cat'),
    path('teacher/<str:teacher>',Maincourse,name='course_teacher'),
    path('search/',Maincourse,name='course_search'),
    path('course_detail/<int:id>',course_detail,name='course_detail'),
    path('<int:id>',delete_comment,name='delete'),
    path('edit/comment/<int:id>',edit,name='edit'),
]