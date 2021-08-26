from basic_app import models
from django.shortcuts import render
#from basic_app import views
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
# Create your views here
#def index(request):
#   return render(request, 'basic_app/index.html')


class IndexView(TemplateView):
    template_name = "basic_app/index.html"


class SchoolListView(ListView):
    model = models.School


class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app /school_detail.html'
