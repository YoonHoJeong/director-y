from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import StaffRegistraionForm, ActorRegistraionForm, DirectorRegistraionForm, ProfileAuthenticationForm
from django.views.generic import CreateView


from .models import Profile
from main.models import Movie, ActorImage, ActorVideo, Filmography

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

# @login_required(login_url='/login/')
def user_page(request, user_id=0):
    # header에서 mypgae 클릭, 자신의 마이페이지로 갈 때
    if user_id:
        # 다른 사람의 user_page에 접근
        user = get_object_or_404(Profile, pk = user_id)
    else:
        # 로그인되지 않았는데 header에서 mypage를 누른 경우 로그인 페이지로 이동
        user = request.user

        if not user.is_authenticated:
            # 로그인되지 않았을 때,
            return redirect('/login')
    profile_user = user

    # user의 portfolio 가져오기
    if profile_user.u_type == 1:
        # 해당 유저가 감독일 경우
        movie_pfs = Movie.objects.filter(director = profile_user.id)
        return render(request, 'user_page.html', {"profile_user": profile_user, "movie_pfs":movie_pfs})
    elif profile_user.u_type == 2:
        # 해당 유저가 배우일 경우
        profile_images = ActorImage.objects.filter(actor = profile_user.id)
        filmos = Filmography.objects.filter(profile = profile_user.id)
        return render(request, 'user_page.html', {"profile_user": profile_user, "profile_images":profile_images, "filmos":filmos})
    elif profile_user.u_type == 3:
        # 해당 유저가 스탭일 경우
        pass
    return redirect('/')

def edit_user(request):
    user = request.user

    user.intro = request.POST.get("intro")
    # user.date_of_birth = request.POST.get("date_of_birth")
    user.education = request.POST.get("education")
    print(request.POST.get("date_of_birth"))

    user.save()
    
    return redirect(f"/user_page/{user.id}")


