from django.db import models

class Services(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class ContactUs(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name