from django.shortcuts import render
from django.utils import timezone
from .models import Post # . means from the same directory (like linux)
# Create your views here.
def post_list(request):
	# posts acts like the name of the QuerySet.
	# request all blog posts with a published date previous to the present time and sorted them in reverse chronological order
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	# render with the current HTTP request param. The last param is a dictionary to add dynamic data.
    return render(request, 'blog/post_list.html', {'posts': posts})