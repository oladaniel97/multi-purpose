from django.shortcuts import render,redirect
import requests
from .models import Todo,Dic,City
from .forms import TodoForm,DicForm,cityform
from pydictionary import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import UserCreation




# Create your views here.
def home(request):
    user_authenticated = request.user.is_authenticated
    context = {
        'user_authenticated': user_authenticated
    }
    return render(request,'index.html',context)

@login_required
@csrf_exempt
def todo(request):
    items = Todo.objects.filter(user=request.user)

    if request.method == 'POST':
        form  = TodoForm(request.POST)
        todo_item = form.save(commit=False)
        todo_item.user = request.user
        todo_item.save()

    form = TodoForm()
    return render(request, 'todo/index.html',{'form':form,'items':items})

def delete(request, id):
    pos=Todo.objects.get(pk=id)
    pos.delete()
    
    
    return redirect('/todo')

@login_required
@csrf_exempt
def dic(request):
    if request.method == 'POST':
        form  = DicForm(request.POST)
        dic_item = form.save(commit=False)
        dic_item.user = request.user
        dic_item.save()
    items = Dic.objects.filter(user=request.user)
    words = []
    for item in items:
        dict = Dictionary(item)
      
        data={
            'id':item.id,
            'word': item.word,
            'meaning': dict.meanings(),
            'synonyms': dict.synonyms(),
            'antonyms': dict.antonyms(),
        }
        # meaning = dict.meanings()
        # mean = dict.print_meanings()
        words.append(data)
    # print(mean)
   
    form = DicForm()

    return render(request,'dic/dic.html',{'form':form,'items':items,'words':words})

def deleted(request, id):
    pos=Dic.objects.get(id=id)
    pos.delete()
    return redirect('/dic')

@login_required
@csrf_exempt
def city(request):
    if request.method == 'POST':
        form  = cityform(request.POST)
        city_item = form.save(commit=False)
        city_item.user = request.user
        city_item.save()
            
            
    
    form = cityform()
    cities = City.objects.filter(user=request.user)
    weather_data = []

    for city in cities:
       
        api_my = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=fd917a564e2a127eb9abf3b5b98603c1".format(city)).json()
        
    #     unx = api_my['sys']['sunrise']
    #     unxs = api_my['sys']['sunset']
    #     date_times = datetime.datetime.fromtimestamp(unxs)
    #     date_time = datetime.datetime.fromtimestamp(unx)
    #     print("Date & Time =>" ,
    # date_time.strftime('%Y-%m-%d %H:%M:%S'))
    #     print(api_my)

        data = {
            'id': city.id,
            'city': city.name,
            'weather_description': api_my['weather'][0]['description'],
            'weather_temp': api_my['main']['temp'],
            'weather_pressure': api_my['main']['pressure'],
            'weather_humidity': api_my['main']['humidity'],
            'weather_icon': api_my['weather'][0]['icon'],
            'country': api_my['sys']['country'],
            # 'sunrise': date_time.strftime('%H:%M:%S'),
            # 'sunset': date_times.strftime('%H:%M:%S')
        }
        weather_data.append(data)

        


    return render(request, 'weather/weat.html', {'weather_data':weather_data,'form':form})

def deleter(request, city):
    pos=City.objects.get(name=city)
    pos.delete()
    
    
    return redirect('/city')

# 


@csrf_exempt
def login_page(request):
    # if request.user.is_authenticated:
    #     return redirect('note:home')
    # else:
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('note:home')
        else:
                messages.info(request, 'Username or Password is incorrect')
    user_authenticated = request.user.is_authenticated
    context = {
        'user_authenticated': user_authenticated
    }
    
    return render(request, 'login.html', context)

    
# def register(request):
#     return render(request, 'registration.html')

@csrf_exempt
def register(request): 
    if request.user.is_authenticated:
        return redirect('note:home')
    else:
        form = UserCreation()  
        if request.method == 'POST':
            form = UserCreation(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user )
                return redirect('note:login')
        context = {'form':form }  
        return render(request, 'signup.html', context) 


def logout_page(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('note:login')