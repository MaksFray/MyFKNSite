from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

logr = logging.getLogger(__name__)

def email_default():
    return User.email

class UserProfiler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Lastname')
    first_name = models.CharField(max_length=100, blank=True, verbose_name='Firsttname')
    mid_name = models.CharField(max_length=100, blank=True,verbose_name='Midname')
    about = models.TextField(default='Some information',verbose_name='Information about You',blank=True)
    image= models.ImageField(blank=True, verbose_name='Avatar', upload_to="userprofile",null=True,)
    email=models.EmailField(default=' ')
    phone_number=models.IntegerField(verbose_name='Phone',default=0,validators=[
            MaxValueValidator(100000000000),
            MinValueValidator(0)
        ])

    def __str__(self):
        return self.user.username

User.profile = property(lambda u: UserProfiler.objects.get_or_create(user=u)[0])


def get_absolute_url(self):
        return "/acc/profile/%i/" % self.id

@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        up = UserProfiler.objects.create(user=kwargs.get('instance'))
        logr.debug("UserProfile created: %s" % up)