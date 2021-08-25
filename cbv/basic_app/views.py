from django.shortcuts import render
#from basic_app import views
from django.views.generic import View
from django.http import HttpResponse
# Create your views here
#def index(request):
#   return render(request, 'basic_app/index.html')


class CBView(View):
    def get(self, request):
        return HttpResponse("Class Based View")
