from django.forms.widgets import PasswordInput
from basic_app.forms import UserForm
from django.shortcuts import render
from basic_app.forms import UserProfileInfoForms
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect, request

# Create your views here.

#template tagging
app_name = 'basic_app'


def index(request):
    return render(request, 'templates/index.html')


def home(request):
    return render(request, "templates/home.html")


def registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForms(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = True
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForms()

    return render(
        request, 'templates/registration.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        })


def relative(request):
    return render(request, 'templates/relative_url_template.html')


def base(request):
    return render(request, 'templates/base.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account not Active')
        else:
            print("someone tried to login and failed")
            print('username:{} and password :{}'.format(username, password))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request, 'templates/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponseRedirect("You are already logged in")
