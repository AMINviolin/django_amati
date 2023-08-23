from django.db import models

class service(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    content = 