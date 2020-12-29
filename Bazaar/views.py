from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "HTML/home/home.html", {
        "hello" : [1,2,3,4,5]
    })