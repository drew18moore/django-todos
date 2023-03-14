from django import forms

class TodoForm(forms.Form):
    body = forms.CharField(max_length=256, label='', widget=forms.TextInput(attrs={"placeholder": "New Todo"}))