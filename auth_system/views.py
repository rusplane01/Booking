from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = CustomUserCreationForm()
    
    return render(request,
                  'auth_sys/register_form.html',
                  {"form": form}
            )
            
def logout_view(request):
    logout(request)            
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user) 
                return redirect('/')
            else:
                messages.error("Wrong password or username")  
    else:
        form = AuthenticationForm()

    return render(
        request,
        "auth_sys/login_form.html",
        {"form":form}
    )