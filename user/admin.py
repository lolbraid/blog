from django.contrib import admin
from .models import Profile
from import_export.admin import ImportExportModelAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('image', 'user', 'bio', 'wibsite_url', 'facebook_url', 'twitter_url', 'instagram_url')
