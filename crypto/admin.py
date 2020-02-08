from django.contrib import admin
from .models import Words
class WordsAdmin(admin.ModelAdmin):
    list_display = ['key','word','is_active']
    
admin.site.register(Words,WordsAdmin)