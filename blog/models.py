from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
	img = models.ImageField(upload_to='',null =True)
	likes = models.IntegerField(null = True,default = 0)
	
	def __str__(self):
	   return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name = "comments")
	text = models.TextField()
	timestamp = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.text
