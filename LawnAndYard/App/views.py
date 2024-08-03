from django.shortcuts import render
from .models import Customer
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'loginForm.html')


def registerdata(request):
    print(request.method)
    print(request.POST)
    name=request.POST.get("name")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    password=request.POST.get("password")
    re_password=request.POST.get("re_password")
    # print(name,email,phone,password,re_password)

    Customer.objects.create(Name=name,Email=email,Contect=phone,Password=password,Re_Password=re_password)
    return render(request, 'dashboard.html')


def dashboard(request):
    return render(request, 'dashboard.html')