from django.contrib import admin
from .models import Profile
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_thumbnail',)
    list_per_page = 1


admin.site.register(Profile, ProfileAdmin)
