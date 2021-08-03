from django.contrib import admin
from rango.models import Category, Page, Video

from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
admin.site.register(Video, VideoAdmin)