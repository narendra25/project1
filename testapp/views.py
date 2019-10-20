from django.shortcuts import render

# Create your views here.
def home__page__view(request):
    return render(request,'testapp/home.html')
def login__page__view(request):
    return render(request,'testapp/login.html')
def application__page__view(request):
    return render(request,'testapp/application.html')
def education__page__view(request):
    return render(request,'testapp/edu.html')
def it__page__view(request):
    return render(request,'testapp/it.html')
