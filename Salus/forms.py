from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelMultipleChoiceField

from Salus import models


class PasswordForm(ModelForm):
    class Meta:
        model = models.Password
        fields = ('title', 'password', 'url', 'notes' )
