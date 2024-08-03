from django.shortcuts import render
from .models import MyCust
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'loginForm.html')


def registerdata(request):
    print(request.method)
    print(request.POST)
    email=request.POST.get("email")
    password=request.POST.get("password")

    MyCust.objects.create(Email=email,Pasword=password)
    return render(request, 'dashboard.html')


def dashboard(request):
    return render(request, 'dashboard.html')