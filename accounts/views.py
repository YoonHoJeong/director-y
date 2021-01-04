from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .forms import ProfileAuthenticationForm, ImageForm, RegistrationForm

from .models import Profile, Actor, Like, Staff
from main.models import Movie, ActorImage, ActorVideo, Filmography, SPortfolio
from main.forms import SectionForm

# Create your views here.

def register(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            # login part
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
        else:
            context['registration_form'] = form

    else: # GET method일 때,
        form = RegistrationForm()
        return render(request, '../templates/register.html', {'form':form})


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
        likes = Like.objects.filter(profile_user = profile_user).count()
        is_like = Like.objects.filter(profile_user = profile_user, user = request.user).count()
        movie_pfs = Movie.objects.filter(director = profile_user.id)
        
        return render(request, 'user_page.html', {"is_like": is_like, "profile_user": profile_user, "movie_pfs":movie_pfs, "likes":likes})
    
    elif profile_user.u_type == 2:
        # 해당 유저가 배우일 경우
        likes = Like.objects.filter(profile_user = profile_user).count()
        is_like = Like.objects.filter(profile_user = profile_user, user = request.user).count()
        profile_images = ActorImage.objects.filter(actor = profile_user.id)
        filmos = Filmography.objects.filter(profile = profile_user.id)
        
        return render(request, 'user_page.html', {"is_like": is_like, "profile_user": profile_user, "profile_images":profile_images, "filmos":filmos, "image_form": image_form, "likes":likes})
    
    elif profile_user.u_type == 3:
        # 해당 유저가 스탭일 경우
        staff_pfs = SPortfolio.objects.filter(uid = profile_user.id)
        return render(request, 'user_page.html', {"profile_user": profile_user, "staff_pfs":staff_pfs})

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

    return redirect('user_page')


@login_required(login_url='/login/')
def likes(request):
    user = request.user

    likes = Like.objects.filter(user = user, type = 0)

    return render(request, 'likes.html', {'likes':likes, 'type':0})

@login_required(login_url='/login/')
def likes_director(request):
    user = request.user

    likes = Like.objects.filter(user = user, type = 1)

    return render(request, 'likes.html', {'likes':likes, 'type':1})

@login_required(login_url='/login/')
def likes_actor(request):
    user = request.user

    likes = Like.objects.filter(user = user, type = 2)

    return render(request, 'likes.html', {'likes':likes, 'type':2})

@login_required(login_url='/login/')
def likes_staff(request):
    user = request.user

    likes = Like.objects.filter(user = user, type = 3)

    return render(request, 'likes.html', {'likes':likes, 'type':3})

@login_required(login_url='/login/')
def add_like(request):
    # print(request.META.get('HTTP_REFERER'))
    prev_url = request.META.get('HTTP_REFERER')
    profile_user_id = int(prev_url.split("/")[-1])

    user = request.user
    profile_user = Profile.objects.filter(id = profile_user_id).first()

    like = Like()
    like.profile_user = profile_user
    like.user = user

    user_type = profile_user.u_type
    like.type = user_type

    # 좋아요 누른 유저 저장
    like.save()

    return redirect(prev_url)

@login_required(login_url='/login/')
def add_like_movie(request):
    prev_url = request.META.get('HTTP_REFERER')
    movie_id = int(prev_url.split("/")[-1])

    user = request.user
    movie = Movie.objects.filter(id = movie_id).first()

    if movie:
        like = Like()
        like.movie = movie
        like.user = user

        user_type = 0
        like.type = user_type

        # 좋아요 누른 유저 저장
        like.save()

    return redirect(prev_url)    

def delete_like(request):
    prev_url = request.META.get('HTTP_REFERER')
    profile_user_id = int(prev_url.split("/")[-1])

    user = request.user

    profile_user = Profile.objects.filter(id = profile_user_id).first()

    like = Like.objects.filter(user = user, profile_user = profile_user).first()

    like.delete()

    return redirect(prev_url)

def delete_like_movie(request):
    prev_url = request.META.get('HTTP_REFERER')
    movie_id = int(prev_url.split("/")[-1])

    user = request.user
    movie = Movie.objects.filter(id = movie_id).first()
    like = Like.objects.filter(user = user, movie = movie).first()
    like.delete()

    return redirect(prev_url)

def staff_create(request) :
    if request.method == "POST":
        filled_form = SectionForm(request.POST, request.FILES)

        if filled_form.is_valid():
            portfolio_id = request.POST.get('portfolio_id')
            if portfolio_id == 'None' :
                staff_id = request.POST.get('staff_id')
                profile = get_object_or_404(Profile, pk=staff_id)
                staff = get_object_or_404(Staff, profile=profile)
                portfolio = SPortfolio(uid = staff, title=request.POST.get('title'), thumbnail=request.POST.get('thumbnail'), content=request.POST.get('content'))
                portfolio.save()
                return redirect('/')

            else :
                portfolio = get_object_or_404(SPortfolio, pk=portfolio_id)
                portfolio.title = request.POST.get('title')
                portfolio.thumbnail = request.POST.get('thumbnail')
                portfolio.content = request.POST.get('content')
                portfolio.save()
                return redirect('/')

        else :
            staff_id = request.POST.get('staff_id')
            section_form = SectionForm()
            
            return render(request, "staff_create.html", {"staff_form": section_form, "staff_id" : staff_id})

def staff_update(request, portfolio_id) :
    section_form = SectionForm()
    portfolio = get_object_or_404(SPortfolio, pk=portfolio_id)
    staff_id = portfolio.uid.profile.id
    return render(request, 'staff_create.html', {'staff_form' : section_form, 'portfolio_id' : portfolio_id, 'staff_id' : staff_id})

def staff_delete(request, portfolio_id) :

    staff_obj = get_object_or_404(SPortfolio, pk=portfolio_id)

    profile_user = staff_obj.uid

    staff_obj.delete()

    staff_pfs = SPortfolio.objects.filter(uid = profile_user)
    
    return render(request, 'user_page.html', {"profile_user": profile_user.profile, "staff_pfs":staff_pfs})
