from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from sorl.thumbnail import get_thumbnail

# from account import settings

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL)
  birthday = models.DateField(blank=True, null=True,)
  photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)



  def __str__(self):
    return 'Profile for user {}'.format(self.user.username)

  def get_thumb(self):
    im = get_thumbnail(self.photo, '190x190', crop='center', quality=99)
    return im.url


