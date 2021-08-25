from django.shortcuts import render
from basic_app import views


# Create your views here
def index(request):
    return render(request, 'basic_app/index.html')
