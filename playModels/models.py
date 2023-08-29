from django.db import models

class Users(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=30)
    ph_number=models.CharField(max_length=11)
# Create your models here.
class Chatroom(models.Model):
    chatRoom_id=models.IntegerField()


