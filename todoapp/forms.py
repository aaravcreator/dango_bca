from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__' 

class TodoSearchForm(forms.Form):
    title = forms.CharField(max_length=100,required=False)