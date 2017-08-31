from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if email:
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError('duplicated Email')
        return email
