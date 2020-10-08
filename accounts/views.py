from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, StaffRegistraionForm, ActorRegistraionForm, DirectorRegistraionForm, ProfileAuthenticationForm
from django.views.generic import CreateView
from .models import Profile

# Create your views here.


def register(request):
    return render(request, '../templates/register.html')


class director_register(CreateView):
    model = Profile
    form_class = DirectorRegistraionForm
    template_name = "../templates/director_register.html"

    def form_valid(self, form):
        profile = form.save()
        login(self.request, profile)
        return redirect('/')


class actor_register(CreateView):
    model = Profile
    form_class = ActorRegistraionForm
    template_name = "../templates/actor_register.html"

    def form_valid(self, form):
        profile = form.save()
        login(self.request, profile)
        return redirect('/')


class staff_register(CreateView):
    model = Profile
    form_class = StaffRegistraionForm
    template_name = "../templates/staff_register.html"

    def form_valid(self, form):
        profile = form.save()
        login(self.request, profile)
        return redirect('/')


def registration_view(request):
    context = {}
    if request.POST:
        form = ActorRegistraionForm(request.POST)
        if form.is_valid():
            form.save()

            # login part
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  # GET request
        form = ActorRegistraionForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = ProfileAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")
    else:
        form = ProfileAuthenticationForm()

    context['login_form'] = form
    return render(request, 'accounts/login.html', context)
