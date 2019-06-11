from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.name).capitalize()


class Building(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    parent = models.ForeignKey('Building', on_delete=models.CASCADE, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.name).title()


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.name).title()


class Item(models.Model):
    date = models.DateField(default=timezone.now, null=False)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, default=42, blank=False,null=False)
    room = models.CharField(max_length=20, blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=1, blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True)
    retrieved = models.BooleanField(default=False)
    image = models.ImageField(upload_to="img/%Y/%m/",blank=True,null=True)
    register_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registered_items", blank=True, null=True)
    retrieve_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="retrieved_items", blank=True, null=True)
    retrieved_date = models.DateField(blank=True, null=True)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('items:show_item', kwargs={'item_id':self.pk})

    def __str__(self):
        return "pk:{} cat:{} col:{}".format(self.pk, self.category, self.color)

