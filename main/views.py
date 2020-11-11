from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

from .models import Movie, Festival, Section, SPortfolio, ActorImage, ActorVideo
from accounts.models import Actor, Staff, Director
from .forms import SectionForm


def section(request):
    all_sections = Section.objects.all()
    return render(request, "section.html", {"all_sections": all_sections})


def section_create(request):
    if request.method == "POST":
        filled_form = SectionForm(request.POST, request.FILES)

        if filled_form.is_valid():
            filled_form.save()
            return redirect('/')

    section_form = SectionForm()
    return render(request, "section_create.html", {"section_form": section_form})


def home(request):
    all_portfolio = Movie.objects.all()

    return render(request, "home.html", {"all_portfolio": all_portfolio})


def actors(request):
    all_portfolio = Actor.objects.all()

    random_portfolio = Actor.objects.all().order_by('?')[:4]
    return render(request, "actors2.html", {"all_portfolio": all_portfolio, "random_portfolio" : random_portfolio})

def staffs(request):
    all_portfolio = SPortfolio.objects.all()
    #random_portfolio = SPortfolio.objects.all().order_by('?')[:1]

    return render(request, "staffs.html", {"all_portfolio": all_portfolio})

def staff_detail(request, staff_profile_id):
    my_staff = get_object_or_404(Staff, pk=staff_profile_id)
    
    return render(request, 'staff_detail.html', {my_staff: my_staff})


def directors(request):

    if request.method == 'POST':
        movie_id = request.POST.get('portfolio-id')

        temp_obj = Movie.objects.filter(id = movie_id).first()
        
        movie_obj = {}

        print(temp_obj)

        movie_obj['uid'] = temp_obj.uid
        movie_obj['title'] = temp_obj.title
        movie_obj['poster'] = temp_obj.poster
        movie_obj['genre'] = temp_obj.genre
        movie_obj['summary'] = temp_obj.summary
        movie_obj['production_year'] = temp_obj.production_year
        movie_obj['title_eng'] = temp_obj.title_eng
        movie_obj['trailer'] = temp_obj.trailer
        movie_obj['trailer_thumbnail'] = temp_obj.trailer_thumbnail
        
        return render(request, 'movie.html', {'movie_obj' : movie_obj})

    all_portfolio = Movie.objects.all()
    return render(request, "directors.html", {"all_portfolio": all_portfolio})


def mypage(request):
    return render(request, "mypage.html")


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

def actordetail(request, actor_profile_id):
    my_actor = get_object_or_404(Actor, pk=actor_profile_id)
    return render(request, 'actordetail.html', {'my_actor' : my_actor})

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

        if title_kr and img and genre and year and summary :
            movie = Movie(
                uid = request.user,
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

            all_portfolio = Movie.objects.all()
            
            return render(request, 'directors.html', {"all_portfolio": all_portfolio})
        else :
            error = 1
            return render(request, 'enroll_movie.html', {"error" : error})

    return render(request, 'enroll_movie.html')

def movie(request):
    return render(request, 'movie.html')