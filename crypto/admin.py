from django.contrib import admin
from .models import Words

def make_active(modeladmin,request,queryset):
    for obj in queryset:
        obj.is_active = True
        obj.save()
make_active.short_description = "Mark selected active"

class WordsAdmin(admin.ModelAdmin):
    list_display = ['key','word','is_active']
    actions = [make_active]
    ordering = ['key']
    
admin.site.register(Words,WordsAdmin)