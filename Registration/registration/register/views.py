from django.shortcuts import render
from .forms import RegisterForm

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            return render(request, "success.html")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})