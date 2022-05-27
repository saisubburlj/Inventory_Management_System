from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.http import HttpResponse

class NewLoginform(forms.Form):
    username = forms.CharField(label="User Id")
    password = forms.CharField(widget=forms.PasswordInput,label="Password",min_length=8)

# Create your views here.
def index(request):
    if request.method == "POST":
        form = NewLoginform(request.post)
        if form.is_valid():
            user = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
        else:
            return(request,"web_app/login.html",{
                "details": form
            })

    return render(request,"web_app/login.html",{
        "details":NewLoginform()
    })

def login(request,username):
    return HttpResponse(f"Please Login into your Account with {username}")

def welcome(request):
    return HttpResponse("You are successfully logged in")