from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        prodt=products.objects.filter(categ=c_page,available=True)
    else:
        prodt=products.objects.all().filter(available=True)
    cat=category.objects.all()
    return render(request,'index.html',{'pr':prodt,'ct':cat})

def prodetails(request,c_slug,p_slug):
    try:
        prod=products.objects.get(categ__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e

    return render(request,'item.html',{'pr':prod})