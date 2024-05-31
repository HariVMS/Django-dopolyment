from django.shortcuts import render
from django.http import HttpResponse
from model_app.forms import UserProfileForm,UserForm
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request,"basic_app/index.html")

@login_required
def special(request):
    return HttpResponse("You Are logged in Sucessfully, Welcom")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    register=False
    if request.method=="POST":
        user_from=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
        if user_from.is_valid() and profile_form.is_valid():
            user=user_from.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if ' picture ' in request.FILES:
                profile.picture = request.FILES[' picture ']

            profile.save()

            register=True

        else:
            print(user_from.errors,profile_form.errors)

    else:
        user_from=UserForm()
        profile_form=UserProfileForm()

    return render(request,"basic_app/register.html",
                  {'user_from':user_from ,'profile_form':profile_form,"register":register})




def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Activated")
        else:
            print("Someone try to login with wrong username and password")

    else:
        return render(request,'basic_app/login.html')
    





