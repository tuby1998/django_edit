from django.shortcuts import render
from django.http import HttpResponse
from ourfirstapp.utils import *


# View act as controller
# Create your views here.

def index(req):
    data = {
        "title": "Home Page",
        "name": "Sujoy",
        "age": 24
    }
    return render(req, 'ourfirstapp/index.html', data)


def aboutus(req):
    return render(req, 'ourfirstapp/about.html')


def dataprocessing(req):
    data = {
        "titleggg": "Data Processing",
    }
    return render(req, 'ourfirstapp/dataprocessing.html', data)


def dataprocesscontroller(req):
    text = req.POST.get("textp")
    v_count = count_vowel(text)
    data = {
        "vowel": v_count,
    }
    return render(req, 'ourfirstapp/dataprocessingresult.html', data)


def travel(req):
    info = [
        {
         "name": "tom",
         "email": "abc@gmail",
         "phone": "8438974934",
         "date": "20/07/20",
         },
        {
          "name": "jack",
           "email": "jack@gmail",
           "phone": "87836974934",
           "date": "20/07/45",
        },
        {
           "name": "ram",
           "email": "abc@gmail",
           "phone": "843897489796",
           "date": "20/07/19",
        },
        {
            "name": "sita",
            "email": "sita@gmail",
            "phone": "8438974934",
            "date": "20/07/10"
        }
    ]
    details = {'infohh': info}
    return render(req, 'ourfirstapp/travel.html', details)
