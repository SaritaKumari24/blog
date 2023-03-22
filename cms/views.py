from django.shortcuts import render

# Create your views here.
from.models import post
def homepage(r):
    return render(r,"index.html", {"posts":post.objects.all()} )