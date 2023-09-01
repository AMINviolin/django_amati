from django.contrib import admin
from .models import Courses

@admin.register(Courses)

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title','status','price']