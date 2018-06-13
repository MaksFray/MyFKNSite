from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.transaction import commit

from user_shop.models import UserProfiler


class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    passw = forms.CharField(widget=forms.PasswordInput, label='Password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfiler
        fields = ('image','first_name','last_name','mid_name','about','phone_number', 'email')
        file = forms.FileField()



class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user