from django.db import models

# Create your models here.

class clubs(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    link=models.TextField()

    def __str__(self):
        return self.title