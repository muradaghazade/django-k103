from django import forms
from accounts.models import User


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
               'class': 'form-control', 
            }
        )
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
               'class': 'form-control', 
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        if password and confirm_password and password != confirm_password:
            self.add_error('password2', "Passwords do not match.")

        return cleaned_data


class LoginForm(forms.ModelForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
               'class': 'form-control', 
               'name': 'password',
            }
        )
    )
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'name':'username'}),
        }