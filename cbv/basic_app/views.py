from django.urls import reverse_lazy
from basic_app import models
from django.shortcuts import render
#from basic_app import views
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
# Create your views here
#def index(request):
#   return render(request, 'basic_app/index.html')


class IndexView(TemplateView):
    template_name = "basic_app/index.html"


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
