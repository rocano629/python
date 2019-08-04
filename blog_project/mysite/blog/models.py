from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(sef):
        return self.comments.filter(approve_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.models.ForeignKey('blog.Post',related_name='comments', on_delete=models.CASCADE)
    author = models.models.CharField(max_length=200)
    text = models.models.TextField("")
    create_date = models.DateTimeField(default=timezone.Now())
    approved_comment = models.BooleanField(default=False)
        

    class approve:
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
    

    def __str__(self):
        return self.text


)