from django.shortcuts import render,HttpResponseRedirect
from .models import Recipee
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
#login required is used to secure (unauthorized routing)
@login_required(login_url='login_page/')
def Recipe(request):
    if request.method=='POST':

        data=request.POST
        nm=data.get("nm")
        info=data.get("info")
        img=request.FILES.get("img")

        Recipee.objects.create(
            nm=nm,
            info=info,
            img=img
        )

        return HttpResponseRedirect('/')
    data=Recipee.objects.all()

    if request.GET.get('Search'):
        # print(request.GET.get('Search'))
         data=data.filter(nm__icontains = request.GET.get('Search'))

    return render(request,'home.html',context={'info':data})


@login_required(login_url='login_page/')
def delete_recipe(request,id):
    data=Recipee.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/')


@login_required(login_url='login_page/')
def update(request,id):
    data=Recipee.objects.get(id=id)

    if request.method=='POST':
        nm=request.POST.get('nm')
        info=request.POST.get('info')
        img=request.FILES.get('img')

        #another way to update data but in this we have to add img all time when we update data
        # data=Recipee(
        #     nm=nm,
        #     info=info,
        #     id=id,
        #    )
        
        data.nm=nm
        data.info=info

        if img:
            data.img=img

        data.save()
        return HttpResponseRedirect('/')
    return render(request,'update.html',context={'info':data})

def login_page(request):
    if request.method=='POST':

        data=request.POST
        username=data.get("username")
        password=data.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid Username!!')
            return HttpResponseRedirect('/login_page')
        
        user= authenticate(username=username, password=password)

        if user is None:
            messages.error(request,'Invalid Password!!')
            return HttpResponseRedirect('/login_page')
        else:
            login(request,user)
            return HttpResponseRedirect('/')
        
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login_page')

def register(request):
    if request.method=='POST':

        data=request.POST
        fname=data.get("fname")
        lname=data.get("lname")
        email=data.get("email")
        username=data.get("username")
        password=data.get("password")

        user = User.objects.filter(username =username)

        if user.exists():
            messages.error(request,'Username already exist!!')
            return HttpResponseRedirect('/register')

        User.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            username=username,
            #this method is used to save password in encrypted mode
            password=make_password(password)
        )

        return HttpResponseRedirect('/register')
    User.objects.all()
    return render(request,'register.html')