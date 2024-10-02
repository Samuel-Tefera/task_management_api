from django.contrib import admin

from .models import User, Task


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    list_filter = ['due_date', 'status', 'priority']


admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
