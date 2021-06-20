from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        # grab and display only the approved comments from list of comments
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    # each comment is linked to a blog post
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse('post_list')
    