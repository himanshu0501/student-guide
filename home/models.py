from django.db import models

# Create your models here.
class Detail(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title