from django.urls import path
from . import views

urlpatterns = [
	path('',views.todo_list,name='todo_list'),
	path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
	path('todo/<int:pk>/statusupdate', views.todo_statusupdate, name='todo_statusupdate'),
	path('todo/clearcompleted', views.todo_clearcompleted, name='todo_clearcompleted'),
	path('todo/clearall', views.todo_clearall, name='todo_clearall'),
	path('todo/new/', views.todo_new, name='todo_new'),
	path('todo/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
	path('todo/<pk>/remove/', views.todo_remove, name='todo_remove'),
]