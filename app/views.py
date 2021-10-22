from django.shortcuts import render
from .models import *

def index(request):
    return render(request, "app/index.html")

def stu_login(request):
    return render(request, "app/stulogin.html")

def lib_login(request):
    return render(request, "app/liblogin.html")

def lib(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        libSet = librarian.objects.all()
        is_there = False
        for f in libSet:
            if f.username == username and f.password == password:
                is_there = True
        if is_there:
            l = libSet.get(username = username)
            return render(request, "app/lib.html" ,{
                "l":l 
            })

def stu(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        stuSet = student.objects.all()
        is_there = False
        for f in stuSet:
            if f.username == username and f.password == password:
                is_there = True
        if is_there:
            l = stuSet.get(username = username)
            return render(request, "app/stu.html" ,{
                "l":l 
            })   

def add(request, un):
    l = librarian.objects.get(username = un)
    return render(request, "app/add.html", {
        "l": l
    })

def add2(request , un):
    if request.method == "POST":
        name = request.POST["name"]
        phoneno = request.POST["phoneno"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        p2 = request.POST["password2"]
        l = librarian.objects.get(username = un)
        if password == p2:
            s = student(name=name, phone_number=phoneno, email_id=email, username=username, password=password)
            s.save()
            return render(request, "app/lib.html", {
                "l":l
            })



