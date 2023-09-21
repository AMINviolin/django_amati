from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse
from course .models import Courses

class StaticSiteMap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'root:home',
            'root:about',
            'root:contact',
            'root:trainer',
            'course:courses',
        ]
    
    def location(self,item):
        return reverse(item)


class DynamicSiteMap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return  Courses.objects.filter(status=True)
    
    def location(self,obj):
        return '/course/course_detail/%s' % obj.id
