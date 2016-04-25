from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Newspaper(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='category1')
    category2 = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='category2')

    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE, default=1)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Feed(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category)
    newspaper = models.ForeignKey(Newspaper)
    url = models.URLField()

    def __unicode__(self):
        return self.title