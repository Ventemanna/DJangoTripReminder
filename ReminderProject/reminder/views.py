from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser


def index(request):
    is_authenticated = request.user.is_authenticated
    return render(request, "reminder/main_page.html", {"is_authenticated": is_authenticated})

def exit_account(request):
    logout(request)
    return redirect(".")

def sign_in(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(username=form.cleaned_data["username"])
            login(request, user)
            return redirect("/")
    else:
        form = UserLoginForm()
    return render(request, "reminder/sign_in_page.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.published_date = timezone.now()
            user.save()

            login(request, user)

            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, "reminder/register_page.html", {"form": form})

@login_required
def profile(request):
    return render(request, "reminder/profile.html", {"user": request.user})

def create_reminder(request):
    if request.method == "POST":
        return redirect('./profile')
    else:
        form = UserRegisterForm()
        return HttpResponse("Create reminder")