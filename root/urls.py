from django.urls import path,include
from root import views

app_name = 'root'

urlpatterns = [
    path("",views.home,name='home'),
    path("about",views.about),
    path("contact",views.contact),
]