from django.shortcuts import render, redirect
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
import requests
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from urllib.request import urlopen
import json
from .models import Acc
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
import yfinance as yf
api_key="09af29ab6806b18e3306fda218cac2d1"
def hello_there(request, name):
    return render(
        request,
        'appEx/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
def stock(request):
    return render(request, "appEx/stock.html")

def stock_info(request, name):
    stock_data=yf.Ticker(name)
    data=(stock_data.history(period="1y", interval="1mo")).to_json(orient='records')
    return render(request, "appEx/stockFormat/"+ name+".html", {'data':data})

def contact(request):
    return render(request, "appEx/contact.html")
def home(request):
    return render(request, "appEx/home.html", {'name': request.session.get('username'), 'balance':request.session.get('balance')})

def signup(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            existing_user = Acc.objects.filter(username=username).exists()
            if existing_user:
                messages.info(request, "Username is already taken")
                return redirect("/signup", )
            password = form.cleaned_data['password']
            hashed_password = make_password(password)
            Acc.objects.create(username=username, password=hashed_password, balance=10000.00)
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, 'appEx/signup.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pw=form.cleaned_data['password']
            try:
                user = Acc.objects.get(username=name)
            except Acc.DoesNotExist:
                messages.info(request, "Incorrect User")
                return redirect("/")
            if check_password(pw,user.password):
                request.session['username']=name
                request.session['balance']=user.balance
                return redirect("/home")
            else:
                messages.info(request, "Incorrect Password")
                return redirect("/")
    else:
        form = LoginForm()
    return render(request, 'appEx/login.html', {'form':form})