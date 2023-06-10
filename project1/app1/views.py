from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")
def hello(request):
    return render(request,"demo.html")
