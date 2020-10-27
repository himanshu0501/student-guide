from django.db import models

# Create your models here.

class Registeration(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField(primary_key=True)
    batch=models.IntegerField()
    address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone_no1=models.IntegerField()
    phone_no2=models.IntegerField()
    hostel=models.CharField(max_length=50)
    roomno=models.IntegerField()


    def __str__(self):
        return self.name