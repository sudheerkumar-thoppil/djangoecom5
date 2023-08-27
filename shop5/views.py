from django.shortcuts import render
from .models import Product5

# Create your views here.
def index(request):
    products=Product5.objects.all()
    return render(request,'index.html',{'products':products})