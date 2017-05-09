from django.contrib import admin
from .models import Post

# customizes the interface
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_date','published_date']

admin.site.register(Post, PostAdmin) # need to register the model to make it visible in the admin page