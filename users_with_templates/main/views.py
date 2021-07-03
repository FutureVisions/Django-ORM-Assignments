from django.shortcuts import render, HttpResponse, redirect
from .models import users
def home(request):
    context = {
        "users": users.objects.all()
    }
    return render(request, "home.html", context)

def new_user(request):
    users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        age = request.POST['age'],
    )
    return redirect('/')
# Create your views here.
