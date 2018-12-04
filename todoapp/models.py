from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
	Todo = models.CharField(max_length=600)
	creationDate = models.DateTimeField(default=timezone.now())
	Status = models.CharField(default='Open',max_length=20)

	def SelfSave(self):
		self.save()

	def __str__(self):
		return self.Todo

