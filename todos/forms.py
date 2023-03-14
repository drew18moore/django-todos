from django import forms

class TodoForm(forms.Form):
    body = forms.CharField(
        max_length=256, 
        label='', 
        widget=forms.TextInput(
            attrs={"placeholder": "New Todo"}
        )
    )

class RegisterForm(forms.Form):
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
    repeat_password = forms.CharField(
        max_length=64,
        label='',
        widget=forms.PasswordInput(
            attrs={"placeholder": "password"}
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