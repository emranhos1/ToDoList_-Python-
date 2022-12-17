from django import forms
from .models import Task


class customCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {
            'title',
            'description',
            'complete'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-control'})
        }
