from django.db import models
import datetime
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Trainer(models.Model):
    info = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    image = models.ImageField(upload_to='trainer',default='teacher.png')
    twitter = models.CharField(max_length=255,default='#')
    facebook = models.CharField(max_length=255,default='#')
    instagram = models.CharField(max_length=255,default='#')
    linkedin = models.CharField(max_length=255,default='#')
    status = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.info.username


class Courses(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=1000)
    teacher = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='courses',default='default.jpg')
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    counted_likes = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    available_seats = models.IntegerField(default = 0)
    schedule = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    
    def snip(self):
        return self.content[:15] + '...'
    
    def capt(self):
        return self.title.capitalize()
    
class Comment(models.Model):
    which_course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name

class Reply(models.Model):
    which_comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name