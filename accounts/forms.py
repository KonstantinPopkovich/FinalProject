from django.forms import ModelForm, CharField, PasswordInput, ValidationError
from django.contrib.auth.models import User

class UserRegistrationForm(ModelForm):
    password = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Repeat password', widget=PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        print(cd["password"])
        if cd['password'] != cd['password2']:
            raise ValidationError("Passwords don't match.")
        return cd['password2']
