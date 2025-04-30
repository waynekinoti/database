from itertools import count

from django.shortcuts import render

from my_app.models import Customer


# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST.get('names')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        weight=request.POST.get('weight')
        height=request.POST.get('height')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        Customer.objects.create(names=name,email=email,phone=phone,weight=weight,height=height,gender=gender,password=password)
        print(f"{count}Customers")
    return render(request, 'home.html')


def show(request):
    data=Customer.objects.all()
    return render(request, 'show.html',{'data':data})