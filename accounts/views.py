from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import StaffRegistraionForm, ActorRegistraionForm, DirectorRegistraionForm, ProfileAuthenticationForm
from django.views.generic import CreateView


from .models import Profile, Actor
from main.models import Movie, ActorImage, ActorVideo, Filmography

from .forms import ImageForm

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

    image_form = ImageForm()

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
        return render(request, 'user_page.html', {"profile_user": profile_user, "profile_images":profile_images, "filmos":filmos, "image_form": image_form})
    elif profile_user.u_type == 3:
        # 해당 유저가 스탭일 경우
        pass
    return redirect('/')

def edit_user(request):
    user = request.user

    user.intro = request.POST.get("intro")
    # user.date_of_birth = request.POST.get("date_of_birth")
    user.education = request.POST.get("education")

    user.save()
    
    return redirect(f"/user_page/{user.id}")


def my_account(request):
    if request.method == "GET":
        return render(request, 'my_account.html')
    else:
        # method가 POST일 때
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        user = request.user

        if name:
            user.name = name
        if email:
            user.email = email
        if phone_number:
            user.phone_number = phone_number

        user.save()

        return redirect('my_account')

def edit_password(request):
    if request.method == "GET":
        return render(request, 'edit_password.html')
    else:
        prev_password = request.POST.get('prev_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        user = request.user
        if request.POST.get("prev_password"):

            user = request.user

            #User entered old password is checked against the password in the database below.
            if user.check_password('{}'.format(prev_password)) == True:
                if new_password1 == new_password2:
                    user.set_password(new_password1)
                    user.save()
                    print("비번 변경", new_password1)
                    logout(request)
                    return redirect('login')

        # user.set_password(new_password1)
        # print(user.password)

        return redirect('edit_password')

def delete_actor_image(request, image_id):
    select_image = ActorImage.objects.filter(id = image_id).first()

    if select_image and request.user == select_image.actor.profile:
        if select_image:
            select_image.delete()
        else:
            redirect('home')
    else:
        return redirect('home')
    return redirect('user_page')


def add_actor_image(request):
    """Process images uploaded by users"""
    actor = Actor.objects.filter(profile = request.user).first()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            actor_image = form.save(commit=False)
            actor_image.actor = actor
            actor_image.save()
            print("success")
            

    return redirect('user_page')