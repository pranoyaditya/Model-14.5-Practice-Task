from django import forms 
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'
        widgets = {
            'BirthDate' : forms.DateInput(attrs={'type': 'date'}),
            'Date_Time' : forms.DateTimeInput(attrs={'type' : 'time'}),
            'Game_Duration' : forms.TextInput(attrs={'type':'duration', 'placeholder': 'HH:MM:SS'}),
            'Bio' : forms.Textarea(attrs={'rows':3})
        }