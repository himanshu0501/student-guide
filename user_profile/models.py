from django.db import models
from django.contrib.auth.models import User
from PIL import Image
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

    def save(self): # here we are overriding the save method of this model
        super().save() # first we have saved the data and now we will grab the
        # image and then decrease its size because large image can make our program quite slow.

        img = Image.open(self.image.path) # here we are opening the image first

        if img.height > 300 or img.width > 300:
            output_size = (300,300)  # if greater size then output_size (300,300)
            img.thumbnail(output_size) # converting image according to size
            img.save(self.image.path)   # saving that image




