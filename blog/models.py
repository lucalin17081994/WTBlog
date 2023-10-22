from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=15, blank=True, null=True)
    language_preference = models.CharField(max_length=10, choices=[('English', 'English'), ('Spanish', 'Spanish')], default='English', blank=True)
    time_zone = models.CharField(max_length=50, blank=True, null=True)
    newsletter_subscription = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create your models here.
class BlogPost(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='blogposts')
    title=models.CharField(max_length=100)
    content = models.TextField()