from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')            
            messages.success(request, f'{username}, Your account has been created')
            return redirect('home')
    else:
        form = UserCreateForm()
    context = {"form": form}
    return render(request, 'register.html', context)


# @login_required()
# def dashboard(request):
#     return render(request, 'User/dashboard.html')