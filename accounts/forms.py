from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.fields import EmailField
from django.core.validators import validate_email

class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'autofocus': 'True'}))
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            }
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # check and raise error if user doesn't input a correct email address
        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError("Not a valid Email Address")
        # check and raise error if other user already exists with given email
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError("User already exists with this email")
        return email

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'autofocus': 'True'}))
    last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = {
            # 'email',
            'first_name',
            'last_name',
            'password'
        }
