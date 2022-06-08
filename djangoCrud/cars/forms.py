from django import forms
from .models import Car
class Create(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'