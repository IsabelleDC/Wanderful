from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from wander.models import Wanderer, Location, Category
from django.contrib.auth.models import User

class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Wanderer
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Wanderer.objects.get(username=username)
        except Wanderer.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

class LocationForm(ModelForm):
    class Meta:
        model = Location

class CategoryForm(forms.Form):
    name = forms.CharField(label="Category")

