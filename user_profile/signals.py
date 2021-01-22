from django.db.models.signals import post_save #signals are used to do the work automatically
# like when user register then automatically we want that user gets its profile 
from django.contrib.auth.models import User # sender is our user who will send the signal 
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=User)  # if user is created then send a signal which will create profile too.
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(User=instance)


@receiver(post_save,sender=User)  # after creating the profile save the profile.
def save_profile(sender,instance,**kwargs):
    instance.profile.save()