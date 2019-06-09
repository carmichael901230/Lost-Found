from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    date = models.DateField(default=timezone.now, null=False)
    building = models.IntegerField(blank=False,null=False, default=0)
    room = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=10,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    category = models.IntegerField(blank=True,null=True)
    retrieved = models.BooleanField(default=False)
    image = models.ImageField(upload_to="img/%Y/%m/",blank=True,null=True)
    register_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registered_items", blank=True, null=True)
    retrieve_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="retrieved_items", blank=True, null=True)
    retrieved_date = models.DateField(blank=True, null=True)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('items:show_item', kwargs={'item_id':self.pk})