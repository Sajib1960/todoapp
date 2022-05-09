from unittest.util import _MAX_LENGTH
from django import forms


class TaskForm(forms.Form):
    text = forms.CharField(max_length=100,
        widget=forms.TextInput(
            attrs={ 'class' : 'form-control', 'placeholder' : 'Enter todo e.g Clean Table',
             'area-lebel' : 'todo', 'area-describeby' : 'add-btn'}
        ))
