from itertools import count

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from my_app.models import Customer
from my_app.my_forms import CustomerForm, LoginForm
from my_app.my_serializers import CustomerSerializer


# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        name = request.POST.get('names')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        Customer.objects.create(names=name, email=email, phone=phone, weight=weight, height=height, gender=gender,
                                password=password)
        print(f"{count}Customers")
    return render(request, 'home.html')

@login_required
def show(request):
    data = Customer.objects.all()
    return render(request, 'show.html', {'data': data})

@login_required
def delete(request, id):
    user = Customer.objects.get(id=id)
    user.delete()
    return redirect('show-page')

@login_required
def details(request, id):
    user = Customer.objects.get(id=id)
    return render(request, 'details.html', {'user': user})

@login_required
def add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show-page')

    else:
        form = CustomerForm()
    return render(request,'forms.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form=LoginForm()
    return render(request, 'signin.html', {'form': form})

@api_view(['GET'])
def api_customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return Response(serializer.data)