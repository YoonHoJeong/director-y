from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

from .models import Movie, Festival, Section, SPortfolio, ActorImage, ActorVideo
from accounts.models import Actor, Staff, Director, Like
from .forms import SectionForm


def section(request):
    all_sections = Section.objects.all()
    return render(request, "section.html", {"all_sections": all_sections})


def section_create(request):
    if request.method == "POST":
        filled_form = SectionForm(request.POST, request.FILES)

        if filled_form.is_valid():
            section_id = request.POST.get('section_id')
            if section_id == 'None' :
                movie_id = request.POST.get('movie_id')
                movie_obj = get_object_or_404(Movie, pk=movie_id)
                section = Section(mid = movie_obj, title=request.POST.get('title'), thumbnail=request.POST.get('thumbnail'), content=request.POST.get('content'))
                section.save()
                return redirect('/')

            else :
                section = get_object_or_404(Section, pk=section_id)
                section.title = request.POST.get('title')
                section.thumbnail = request.POST.get('thumbnail')
                section.content = request.POST.get('content')
                section.save()
                return redirect('/')

        else :
            movie_id = request.POST.get('movie_id')
            movie_obj = get_object_or_404(Movie, pk=movie_id)
            section_form = SectionForm()
            
            return render(request, "section_create.html", {"section_form": section_form, "movie_obj" : movie_obj})

    section_form = SectionForm()
    return render(request, "section_create.html", {"section_form": section_form})

def section_detail(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    return render(request, "section_detail.html", {"section" : section})

def section_update(request, section_id) :
    section_form = SectionForm()
    return render(request, "section_create.html", {"section_form" : section_form, "section_id" : section_id})

def section_delete(request, section_id) :

    section_obj = get_object_or_404(Section, pk=section_id)
    movie_obj = section_obj.mid
    section_obj.delete()
    sections = Section.objects.filter(mid = movie_obj)

    print(section_id)

    return render(request, "movie.html", {"movie_obj" : movie_obj , "sections" : sections})

def home(request):
    movies = Movie.objects.all()
    actors = Actor.objects.all()

    return render(request, "home.html", {"movies": movies, "actors":actors})


def staffs(request):
    staffs = SPortfolio.objects.all()

    return render(request, "staffs.html", {"all_portfolio": staffs})

def staff_detail(request, staff_profile_id):
    my_staff = get_object_or_404(Staff, pk=staff_profile_id)
    
    return render(request, 'staff_detail.html', {my_staff: my_staff})


def directors(request):

    if request.method == 'POST':
        movie_id = request.POST.get('portfolio-id')

        movie_obj = get_object_or_404(Movie, pk=movie_id)

        sections = Section.objects.filter(mid = movie_obj)
        
        return render(request, 'movie.html', {'movie_obj' : movie_obj, "sections":sections})

    all_portfolio = Movie.objects.all()
    return render(request, "directors.html", {"all_portfolio": all_portfolio})

def movie_detail(request, movie_id):
    movie_obj = get_object_or_404(Movie, pk=movie_id)
    sections = Section.objects.filter(mid = movie_obj)
    director = Director.objects.filter(profile = movie_obj.director).first()
    likes = Like.objects.filter(movie = movie_obj).count()
    is_like = Like.objects.filter(movie = movie_obj, user=request.user).count()

    return render(request, "movie.html", {"is_like":is_like, "movie_obj":movie_obj, "sections":sections, "likes":likes, "director" : director})

def new(request):
    return render(request, 'create.html')

def create(request):
    return render(request, 'create.html')

    if request.method == 'POST':
        portfolio = Portfolio()
        portfolio.title = request.POST['title']
        portfolio.save()

        section_titles = request.POST.getlist('section-title')
        section_texts = request.POST.getlist('section-text')

        section_len = len(section_titles)

        for i in range(section_len):
            section = Section()
            section.portfolio = portfolio

            # image가 필수가 아닐 때, 순서 어떻게 찾을 것인지?
            # 따로 input id를 설정해야할듯.
            # if 'section-image' in request.FILES:
            #     section.image = request.FILES['section-image'][i]
            section.title = section_titles[i]
            section.text = section_texts[i]
            section.save()

        # section 개수 만큼 section 생성.

        # portfolio 먼저 생성
        # 생성되는 portfolio id 받고
        # portfolio id를 foreign key로 넣은 section 생성.

        # print(request.FILES)

        return redirect("home")

def enroll_movie(request):

    if request.method == "POST" :
        title_kr = request.POST.get('title-kr')
        title_en = request.POST.get('title-en')
        img = request.POST.get('img')
        trailer = request.POST.get('trailer')
        genre = request.POST.get('genre')
        year = request.POST.get('year')
        summary = request.POST.get('summary')
        trailer_thum = request.POST.get('trailer-thum')
        movie_id = request.POST.get('movie-id')

        if movie_id == 'None' :

            if title_kr and img and genre and year and summary :
                movie = Movie(
                    director = request.user,
                    title = title_kr,
                    title_eng = title_en,
                    poster = img,
                    trailer = trailer,
                    trailer_thumbnail = trailer_thum,
                    genre = genre,
                    summary = summary,
                    production_year = year
                )        

            print(img)
                
            movie.save()   

        else :
            movie = Movie.objects.get(id = movie_id)
            movie.title = title_kr
            movie.title_eng = title_en
            movie.poster = img
            movie.trailer = trailer
            movie.trailer_thumbnail = trailer_thum
            movie.genre = genre
            movie.summary = summary
            movie.production_year = year
            movie.save()
            
        all_portfolio = Movie.objects.all() # director로 안 넘어가게?
            
        return render(request, 'directors.html', {"all_portfolio": all_portfolio})
    #else :
    #    error = 1
    #    return render(request, 'enroll_movie.html', {"error" : error})

    return render(request, 'enroll_movie.html')

def update_movie(request, movie_id) :

    movie_obj = get_object_or_404(Movie, pk = movie_id)

    return render(request, 'enroll_movie.html', {'movie_obj' : movie_obj})

def delete_movie(request, movie_id) :

    movie_obj = get_object_or_404(Movie, pk = movie_id)
    movie_obj.delete()

    return render(request, 'directors.html')

def movie(request):
    return render(request, 'movie.html')

def actors(request):
    actors = Actor.objects.all()

    random_actors = Actor.objects.all().order_by('?')[:4]
    
    return render(request, "actors.html", {"actors": actors, "random_actors" : random_actors})

def actor_detail(request, actor_id):
    my_actor = get_object_or_404(Actor, pk=actor_id)

    return render(request, 'actor_detail.html', {'my_actor' : my_actor})

