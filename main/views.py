from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

from .models import Movie, Festival, Section, SPortfolio, ActorImage, ActorVideo
from accounts.models import Actor


def home(request):
    all_portfolio = Movie.objects.all()

    return render(request, "home.html", {"all_portfolio": all_portfolio})


def actors(request):
    all_portfolio = Actor.objects.all()
    random_portfolio = Actor.objects.all().order_by('?')[:4]
    return render(request, "actors2.html", {"all_portfolio": all_portfolio, "random_portfolio" : random_portfolio})


def staffs(request):
    all_portfolio = SPortfolio.objects.all()

    return render(request, "home.html", {"all_portfolio": all_portfolio})


def directors(request):
    all_portfolio = Movie.objects.all()
    return render(request, "home.html", {"all_portfolio": all_portfolio})


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
