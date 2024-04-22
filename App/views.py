# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django.core.paginator import Paginator
from . models import Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)   
        redirect('/')
    return render(request, 'login.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            return HttpResponse("Password not same Try Again!!..")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            # return HttpResponse("User had been Created Successfully !!")
            return redirect('/')
        print(uname,email,pass1,pass2)
    return render(request,'signup.html')

def logout_user(request):
    logout(request)
    return redirect("/")