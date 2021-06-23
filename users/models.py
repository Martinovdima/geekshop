from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'pk': self.pk})
