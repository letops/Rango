from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from Base import models


class RangoUserSignForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = models.RangoUser
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            models.RangoUser._default_manager.get(username=username)
        except models.RangoUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2 or password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class RangoUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label='password', help_text="""Raw passwords are not stored.""")

    class Meta(UserChangeForm.Meta):
        model = models.RangoUser
        fields = ('username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'user_permissions')

    def clean_password(self):
        return self.initial['password']