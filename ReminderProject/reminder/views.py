from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import UserForm
from .models import CustomUser


def index(request):
    return render(request, "reminder/main_page.html")

def sing_in(request):
    return HttpResponse("Sing in")

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.published_date = timezone.now()
            user.save()

            login(request, user)

            return redirect('.')
        else:
            return render(request, "reminder/register_page.html", {"form": form})
    else:
        form = UserForm()
        return render(request, "reminder/register_page.html", {"form": form})

@login_required
def profile(request):
    return render(request, "reminder/profile.html", {"user": request.user})

def create_reminder(request):
    if request.method == "POST":
        return redirect('./profile')
    else:
        form = ReminderForm()
        return HttpResponse("Create reminder")