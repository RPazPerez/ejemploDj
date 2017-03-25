from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Bathroom(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    container = models.CharField(max_length=25)
    water_amount_container = models.FloatField()
    wateringcan = models.CharField(max_length=25)
    water_amount_wateringcan = models.FloatField()
    bathtub = models.CharField(max_length=25)
    water_amount_bathtub = models.FloatField()
    handwash = models.CharField(max_length=25)
    water_amount_handwash = models.FloatField()
    date = models.DateField()

class Action(models.Model):
    ACTION_TYPE = (
        ("B","Banarse"),
        ("D1","Descarga_1"),
        ("D2","Descarga_2"),
        ("D3","Descarga_3"),
        ("LD","Lavarse Dientes"),
        ("LM","Lavarse Manos"),
        ("LC","Lavarse Cara"),
    )
    name = models.CharField(max_length=25, choices=ACTION_TYPE)
    bathroom_saving = models.BooleanField()
    date = models.DateField()

class Consumption(models.Model):
    action_id = models.OneToOneField(Action, on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    concluded = models.BooleanField()
    liters_consumed = models.FloatField()
    created = models.DateField()

class Group(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created = models.DateField()

class Medal(models.Model):
    name = models.CharField(max_length=40)
    liter_quantity = models.FloatField()

class Tip(models.Model):
    description = models.CharField(max_length=50)
    action_id = models.OneToOneField(Action, on_delete=models.CASCADE)

class User_Medal(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    medal_id = models.OneToOneField(Medal, on_delete=models.CASCADE)
    created = models.DateField()

class User_Group(models.Model):
    group_id = models.OneToOneField(Group, on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
