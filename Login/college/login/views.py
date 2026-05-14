from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        return render(request,'success.html')
    return render(request,'index.html')