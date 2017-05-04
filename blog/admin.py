from django.contrib import admin
from .models import Post

admin.site.register(Post) # need to register the model to make it visible in the admin page