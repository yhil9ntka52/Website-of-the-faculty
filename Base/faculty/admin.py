from django.contrib import admin
from .models import Department, Program, Teacher, MainPageContent

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'coordinator_name', 'coordinator_contact', 'department')
    search_fields = ('name', 'code', 'coordinator_name')
    list_filter = ('department',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'degree', 'department')
    search_fields = ('name', 'position', 'degree')
    list_filter = ('department',)

@admin.register(MainPageContent)
class MainPageContentAdmin(admin.ModelAdmin):
    list_display = ('content',)
