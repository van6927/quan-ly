from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import admin_required
import csv
from excel_response import ExcelResponse

# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            return redirect('login')
    context ={'form':form}
    return render(request, 'register.html', context)
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                # Nếu là admin, chuyển hướng đến trang admin
                return redirect('admin:index')
            else:
                # Nếu là người dùng bình thường, chuyển hướng đến trang chủ
                return redirect('home')

    context = {}
    return render(request, 'login.html', context)
def home(request):
    return render(request, 'home.html')

@login_required
@admin_required
def admin_dashboard(request):
    # Nội dung trang dashboard cho admin
    admin_url = reverse('admin:index')
    return render(request, admin_url)
