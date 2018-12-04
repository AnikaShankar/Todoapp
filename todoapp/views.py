from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Todo
from .forms import AddTodo


# Create your views here.
def todo_list(request):
	todos = Todo.objects.all().order_by('creationDate')
	if request.method == "POST":
		form = AddTodo(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.Status = 'Open'
			todo.save()
			return redirect('todo_list')
	else:
		form = AddTodo()
		return render(request, 'todoapp/todo_list.html', {'form': form, 'todos' : todos})


def todo_detail(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	return render(request, 'todoapp/todo_detail.html', {'todo': todo})

def todo_new(request):
	if request.method == "POST":
		form = AddTodo(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.Status = 'Open'
			todo.save()
			return redirect('todo_list')
	else:
		form = AddTodo()
		return render(request, 'todoapp/todo_list.html', {'form': form})
		
def todo_edit(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	if request.method == "POST":
		form = AddTodo(request.POST, instance = todo)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.Status = 'Open'
			todo.save()
			return redirect('todo_list')
	else:
		form = AddTodo(instance=todo)
		return render(request, 'todoapp/todo_edit.html', {'form': form})

def todo_remove(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')

def todo_statusupdate(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	if todo.Status == 'Open':
		todo.Status = 'Completed'
	else:
		todo.Status = 'Open'
	todo.save()
	return redirect('todo_list')

def todo_clearcompleted(request):
	todos = Todo.objects.all().filter(Status='Completed').delete()
	return redirect('todo_list')

def todo_clearall(request):
	todos = Todo.objects.all().delete()
	return redirect('todo_list')