from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,"project1app/project1app.html")
    
def index(request):
    return render(request,"project1app/project2.html")
    
