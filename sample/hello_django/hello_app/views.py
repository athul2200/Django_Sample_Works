from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_hello(request):
    movie_data={
        'movies':[{
        'title':'Naran',
        'year':1990,
        'success':False
    },
    {
        'title':'Titanic',
        'year':2000,
        'summary':'story of naran',
        'success':False
    },
    {
        'title':'Lucifer',
        'year':2022,
        'summary':'story of naran',
        'success':False
    },
    
    ]}
    return render(request,'hello.html',movie_data)


