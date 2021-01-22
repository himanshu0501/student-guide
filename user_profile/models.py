from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics') # this upload to tells us the directory name where all the user profile pics will be saved so 
    # this upload_to will create a directory in our project and save all the pics in there but that will flood our main directory with lots of images and we don't want that 
    # so we will change this directory path manually 
    # FOR performance these files stored on the directory rather than the database 
    # we have specify the MEDIA_ROOT in settings which will define the directory name where these pics will be saved 
    # we have specify the MEDIA_URL in settings which will define the URL to access those profile pics 

    def __str__(self):
        return f'{self.user.username} Profile'
