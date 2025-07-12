from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # Title (unique) of the Blog post
    slug = models.SlugField(max_length=200, unique=True) # URL shorthand for URL generation
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts" # Author is the posting User
    )
    content = models.TextField() # The blog article content
    created_on = models.DateTimeField(auto_now_add=True) # The timestamp
    status = models.IntegerField(choices=STATUS, default=0) # Status of the blog post - status is constant as defined - 0 = draft - 1 = published
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter" # Author is the posting User
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)