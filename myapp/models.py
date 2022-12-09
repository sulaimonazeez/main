from django.db import models

class Uploader(models.Model):
  title = models.CharField(max_length=255)
  file = models.FileField(upload_to='myapp/static')
  date = models.DateTimeField(auto_now=True)
  describtion = models.TextField()
  
class Test(models.Model):
  title = models.CharField(max_length=255)
  file = models.CharField(max_length=255)
  date = models.CharField(max_length=255)
  def __str__(self):
    return self.title