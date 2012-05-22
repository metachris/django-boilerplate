from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=3)
    email = forms.EmailField()
    password = forms.CharField(
            widget=forms.PasswordInput(render_value=False), min_length=5)
    password_again = forms.CharField(
            widget=forms.PasswordInput(render_value=False), min_length=5)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        # Check that double passwords match
        pwd1 = cleaned_data.get("password")
        pwd2 = cleaned_data.get("password_again")
        if pwd1 != pwd2:
            raise forms.ValidationError("The passwords don't match.")

        # Check if valid username
        username = cleaned_data.get("username")
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Username is already taken.")
        except User.DoesNotExist:
            pass

        return cleaned_data
