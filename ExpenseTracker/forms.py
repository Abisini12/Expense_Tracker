from django import forms
from django.core.validators import MinLengthValidator
from .models import Userinfo

class UserinfoForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['username', 'name', 'email', 'role', 'password', 'cpassword']

    username = forms.CharField(
        max_length=255,
        required=False,
        validators=[MinLengthValidator(limit_value=10, message='Ensure this field has at least 10 characters.')]
    )
    
    name = forms.CharField(
        max_length=255,
        required=False,
        validators=[MinLengthValidator(limit_value=5, message='Ensure this field has at least 5 characters.')]
    )
    
    password = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(limit_value=8, message='Ensure this field has at least 8 characters.')]
    )

    cpassword = forms.CharField(max_length=255, required=False, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        cpassword = cleaned_data.get('cpassword')

        if password and cpassword and password != cpassword:
            raise forms.ValidationError("Passwords do not match.")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Add custom email validation if needed
            pass
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password



class DateRangeForm(forms.Form):
    # start_date = forms.DateField(label='Start Date', widget=forms.TextInput(attrs={'class': 'datepicker'}))
    # end_date = forms.DateField(label='End Date', widget=forms.TextInput(attrs={'class': 'datepicker'}))
    start_date = forms.DateField(label='Start Date',required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date',required=False, widget=forms.DateInput(attrs={'type': 'date'}))
  