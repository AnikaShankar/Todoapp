from django import forms
from .models import Todo
from django.utils import timezone


class AddTodo(forms.ModelForm):
	
	class Meta:
		model = Todo
		fields = ('Todo',)
