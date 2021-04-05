from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"sample_app1.html")
def sample(request):
    return HttpResponse("<h1>welcome to app1</h1>")