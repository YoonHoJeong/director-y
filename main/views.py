from django.shortcuts import render
# Create your views here.

from .models import Portfolio


def home(request):
    all_portfolio = Portfolio.objects.all()

    return render(request, "home.html", {"all_portfolio": all_portfolio})


def create(request):
    if request.method == 'POST':
        portfolio = Portfolio()
        portfolio.title = request.POST['title']
        # portfolio 먼저 생성
        # 생성되는 portfolio id 받고
        # portfolio id를 foreign key로 넣은 section 생성.
        # section = Section()
        # section.title = request.POST['section-title']
        # section.title = request.POST['section-title']
        # section.title = request.POST['section-title']

    return render(request, 'create.html')
