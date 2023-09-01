from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=1000)
    trainer = models.CharField(max_length=50)
    counted_views = models.IntegerField(default=0)
    counted_like = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    price = models.IntegerField()

    def __str__(self):
        return self.title