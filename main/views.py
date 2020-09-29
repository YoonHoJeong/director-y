from django.shortcuts import render, redirect
# Create your views here.

from .models import Portfolio, DPortfolio, APortfolio, SPortfolio, Section
from accounts.models import Actor

def home(request):
    all_portfolio = DPortfolio.objects.all()

    return render(request, "home.html", {"all_portfolio": all_portfolio})

def home_actor(request):
    all_portfolio = Actor.objects.all()

    return render(request, "home.html", {"all_portfolio": all_portfolio})

def home_staff(request):
    all_portfolio = SPortfolio.objects.all()

    return render(request, "home.html", {"all_portfolio": all_portfolio})    

def new(request):
    return render(request, 'create.html')


def create(request):

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
