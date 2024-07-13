# from django import forms
# from django.contrib.auth.models import User

# class RegisterForm(forms.ModelForm):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_confirm = cleaned_data.get("password_confirm")

#         if password != password_confirm:
#             raise forms.ValidationError("Passwords do not match")

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'preview']

