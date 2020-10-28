from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Boards(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    manufacturer_name = models.CharField(max_length=100)
    last_updated = models.DateTimeField()


    def __str__(self):
        return self.name

    


class Button(models.Model):
    Board = models.ForeignKey(Boards, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    pin_no = models.IntegerField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.name

    


