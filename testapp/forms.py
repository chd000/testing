from .models import CustomUser
from django.forms import ModelForm
from django import forms
from .impclasses import *
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField


class CBForm(forms.Form):
    pass
   # ans = forms.MultipleChoiceField(required=False, label=quest.get_question(), widget=forms.CheckboxSelectMultiple,
    #                                choices=quest.get_answers())


class SeqForm(forms.Form):
    pass
    #ans = forms.MultipleChoiceField(required=True, label=quest.get_question(), widget=forms.Select,
    #                                choices=quest.get_answers())


class UserRegistrationForm(UserCreationForm, ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'last_name', 'first_name']


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'last_name', 'first_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'active', 'admin', 'last_name', 'first_name')

    def clean_password(self):
        return self.initial["password"]
