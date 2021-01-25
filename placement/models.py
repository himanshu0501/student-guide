from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone # imported to show the current time.
# the inbuilt user model in django cannot be extended directly so here we are making another model and connecting this model with user
# Create your models here.
class Extendeduser(models.Model): # Here we are taking models
    user = models.OneToOneField(User,on_delete=models.CASCADE) # here we are connecting this user with the user that we get inbuilt in django form
    name = models.CharField(max_length=20)
    birth_date = models.DateField()  
    batch = models.IntegerField()
    address = models.TextField() # there different fields we can use in our form you can see the document of django for more information about the field and their details.
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    hostel = models.CharField(blank=True,null=True,max_length=50)
    hostel_room = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f'Post title - {self.title}'

        # we will use reverse function it will return the url as a string

    def get_absolute_url(self):
        return reverse('blog',kwargs={'pk':self.pk})  # it will be used to pass the url to createView and that will redirect us to detailview page 
