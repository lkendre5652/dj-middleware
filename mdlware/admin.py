from django.contrib import admin
from .models import Student, Student1
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_field = ['id', 'name']

admin.site.register(Student, StudentAdmin)


class StudentAdmin1(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_field = ['id', 'name']

admin.site.register(Student1, StudentAdmin1)