from django import forms
from .models import Section
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class SectionForm(forms.ModelForm):

    content = SummernoteTextFormField()

    class Meta:
        model = Section
        fields = ('title', 'thumbnail', 'content')
