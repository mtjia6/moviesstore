from django.contrib import admin
from .models import Movie, Review, Report

class MovieAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ["name"]

class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'review', 'user', 'date']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Report, ReportAdmin)
