from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

from .models import Movie, Festival, Section, SPortfolio, ActorImage, ActorVideo
from accounts.models import Actor
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
    movies = Movie.objects.all()
    actors = Actor.objects.all()

    return render(request, "home.html", {"movies": movies, "actors":actors})



def staffs(request):
    staffs = SPortfolio.objects.all()
    random_portfolio = SPortfolio.objects.all().order_by('?')[:1]

    return render(request, "staffs.html", {"staffs": staffs})

def staff_detail(request, staff_profile_id):
    my_staff = get_object_or_404(Staff, pk=staff_profile_id)
    
    return render(request, 'staff_detail.html', {my_staff: my_staff})


def directors(request):
    all_portfolio = Movie.objects.all()
    return render(request, "directors.html", {"all_portfolio": all_portfolio})

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

def actors(request):
    actors = Actor.objects.all()
    print(actors[0].pk)

    random_actors = Actor.objects.all().order_by('?')[:4]
    
    return render(request, "actors.html", {"actors": actors, "random_actors" : random_actors})

def actor_detail(request, actor_id):
    my_actor = get_object_or_404(Actor, pk=actor_id)

    return render(request, 'actor_detail.html', {'my_actor' : my_actor})
