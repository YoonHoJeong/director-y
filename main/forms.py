from django import forms
from .models import Portfolio, Section


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        field = ('', 'content_image', 'content_text')
