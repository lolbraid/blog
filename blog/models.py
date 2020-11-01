from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
# from user.urls import lts

class Category(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='العنوان')
    content = RichTextField(blank=True, null=True, verbose_name='المحتوى')
    help_img = models.ImageField(null=True, blank=True, upload_to = 'posts_header/', verbose_name='الصورة')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='الكاتب')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='التصنيف')
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_posts', verbose_name='الاعجابات')

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])

    class Meta:
        ordering = ('-post_date', )


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الإلكتروني')
    body = models.TextField(verbose_name='التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'علق {} على {}.'.format(self.name, self.post)

    class Meta:
        ordering = ('-comment_date',)
