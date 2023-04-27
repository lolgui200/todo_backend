from django.contrib import admin

from todo.models import Todo

@admin.register(Todo)
class GenericAdmin(admin.ModelAdmin):
    pass
