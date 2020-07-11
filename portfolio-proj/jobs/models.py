from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    detail_image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    summary = models.CharField(max_length=200)
    details = models.CharField(max_length=2500)
    
    def __str__(self):
        return self.name

# class Detail(models.Model):
#     image = models.ImageField(upload_to='images/')
#     name = models.CharField(max_length=100)
#     details = models.CharField(max_length=1000)

#     def __str__(self):
#         return self.name
    
