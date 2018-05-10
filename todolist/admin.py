from django.contrib import admin
from .models import TodoList
from django.contrib.auth.models import User

class TodoListDetail(admin.ModelAdmin):
    list_display = [ 'name', 'user', 'created', 'status', 'expire']

admin.site.register(TodoList, TodoListDetail)
