from django.shortcuts import render,redirect
import requests
from .models import Todo,Dic,City
from .forms import TodoForm,DicForm,cityform
from pydictionary import *
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home(request):
    return render(request,'index.html',{})

@csrf_exempt
def todo(request):
    items = Todo.objects.all()

    if request.method == 'POST':
        form  = TodoForm(request.POST)
        form.save()

    form = TodoForm()
    return render(request, 'todo/index.html',{'form':form,'items':items})

def delete(request, id):
    pos=Todo.objects.get(pk=id)
    pos.delete()
    
    
    return redirect('/todo')

@csrf_exempt
def dic(request):
    if request.method == 'POST':
        form  = DicForm(request.POST)
        form.save()
    items = Dic.objects.all()
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


@csrf_exempt
def city(request):
    if request.method == 'POST':
        form  = cityform(request.POST)
        form.save()

    form = cityform()
    cities = City.objects.all()
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

        if city is  weather_data:
            pass



    return render(request, 'weather/weat.html', {'weather_data':weather_data,'form':form})

def deleter(request, city):
    pos=City.objects.get(name=city)
    pos.delete()
    
    
    return redirect('/city')