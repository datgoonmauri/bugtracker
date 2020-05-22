from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import CustomUser


class SignupForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'display_name', 'password1')


class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput)


class TicketsForm(forms.Form):
	title = forms.CharField(max_length=50)
	description = forms.CharField(widget=forms.Textarea)