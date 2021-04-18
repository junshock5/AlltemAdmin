from django.contrib import admin

from admin.backend.models import Todo


@admin.register(Todo)
class TodoAdmin(Todo.ModelAdmin):
    list_display = ('id', 'name', 'todo')
