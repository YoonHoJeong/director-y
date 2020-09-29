from django.contrib import admin

from .models import Portfolio, DPortfolio, APortfolio, SPortfolio, Section

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(DPortfolio)
admin.site.register(APortfolio)
admin.site.register(SPortfolio)
admin.site.register(Section)
