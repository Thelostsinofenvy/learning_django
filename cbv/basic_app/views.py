from django.shortcuts import render
#from basic_app import views
from django.views.generic import View, TemplateView
# Create your views here
#def index(request):
#   return render(request, 'basic_app/index.html')


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection!'
        return context
