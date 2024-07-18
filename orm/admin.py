from django.contrib import admin
from .models import Student, Region

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'region', 'joined_at')
    list_filter = ('region', 'joined_at')
    search_fields = ('first_name', 'last_name', 'phone')
    ordering = ('-joined_at',)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
