from django import forms

from .models import Food

class DateInput(forms.DateInput):
    input_type = 'date'

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'name',
            'best_before',
            'memo',
        ]
        widgets = {
            'best_before':DateInput(),
        }
