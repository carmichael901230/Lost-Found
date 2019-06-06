from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    building = models.CharField(max_length=20, blank=True,null=True)
    room = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=10,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    category = models.IntegerField(blank=True,null=True)
    retrieved = models.BooleanField(default=False)
    image = models.ImageField(upload_to="img/%Y/%m/",blank=True,null=True)
    register_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registered_items", blank=True, null=True)
    retrieve_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="retrieved_items", blank=True, null=True)

    objects = models.Manager()
