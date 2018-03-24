from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank=True,null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    Post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length = 30)
    text = models.TextField()
    date = models.DateTimeField(default = timezone.now())
    approved = models.BooleanField(default = False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved=True
        self.save()
        print('comment approved!')

    def get_absolute_url(self):
        return reverse('blog:post_list')

