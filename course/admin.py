from django.contrib import admin
from .models import Courses

@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['status','price']
    search_fields = ['title']
