from django import forms

class TodoForm(forms.Form):
    body = forms.CharField(
        max_length=256, 
        label='', 
        widget=forms.TextInput(
            attrs={"placeholder": "New Todo"}
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        label='',
        widget=forms.TextInput(
            attrs={"placeholder": "username"}
        )
    )
    password = forms.CharField(
        max_length=64,
        label='',
        widget=forms.PasswordInput(
            attrs={"placeholder": "password"}
        )
    )