from django import forms
from .models import Section
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ['title', 'thumbnail', 'content']
        widgets = {
            'content' : SummernoteWidget()
        }
