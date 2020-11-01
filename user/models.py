from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.urls import reverse
from ckeditor.fields import RichTextField

class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics' , verbose_name='الصورة الشخصية ')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='المستخدم')
    bio = RichTextField(verbose_name='الوصف')
    wibsite_url = models.CharField(max_length=255, null=True, blank=True, help_text='لا تنسى وضع https://', verbose_name='رابط الموقع')
    facebook_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='facebook')
    twitter_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='twitter')
    instagram_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='instagram')

    def __str__(self):
        return '{} profile.'.format(self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    
    def get_absolute_url(self):
        return reverse('home')


def create_profile(sender, **kwarg):
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])


post_save.connect(create_profile, sender=User)
