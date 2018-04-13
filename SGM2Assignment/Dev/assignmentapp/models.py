from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
	message = models.TextField(max_length=4000)
	last_updates = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, related_name='comments')
	def __str__(self):
		return self.message