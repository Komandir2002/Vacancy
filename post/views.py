from django.shortcuts import render, get_list_or_404
from . import models

# Create your views here.

def all_posts(request):
    data = models.Post.objects.all()
    return render(request,"posts.html",{"posts":data})


def get_vacancy_detail(request,id):
    object = get_list_or_404(models.Post,id=id)             
    return render(request,"show_detail.html",{"show":object})