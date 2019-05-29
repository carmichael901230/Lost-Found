from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    location = models.TextField(blank=True,null=True)
    color = models.CharField(max_length=10,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    category = models.CharField(max_length=20,blank=True,null=True)
    retrieved = models.BooleanField(default=False)
    image = models.ImageField(upload_to="img/%Y/%m/%d/",blank=True,null=True)

