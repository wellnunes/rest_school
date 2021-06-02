from django.contrib import admin
from .models import Course, Rating


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'updated_at', 'status')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'rating', 'created_at', 'updated_at', 'status')
