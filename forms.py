from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _


class UserCreateForm(UserCreationForm):
    '''
    Creates a new user.
    '''
    email = forms.EmailField(label=_('email'), required=True)
    fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        '''
        Saves the new user in database.
        '''
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user