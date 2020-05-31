from django.contrib import admin
from .models import Post, LikeUnlike, UserActivity

class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'activity_date', 'endpoint')
    list_display_links = None

admin.site.register(Post)
admin.site.register(LikeUnlike)
admin.site.register(UserActivity, UserActivityAdmin)
