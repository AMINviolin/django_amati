from django.db import models

class WebDevelopment(models.Model):
    course_name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.course_name

class Marketing(models.Model):
    course_name = models.CharField(max_length=50)
    price = models.IntegerField()   

    def __str__(self):
        return self.course_name
    
class Content(models.Model):
    course_name = models.CharField(max_length=50)
    price = models.IntegerField()   

    def __str__(self):
        return self.course_name


