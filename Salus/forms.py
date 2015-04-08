from django.forms import ModelForm
from django.forms import widgets
from django.db import models as base_m
from django.forms.models import ModelMultipleChoiceField

from Salus import models


class PasswordForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
            if self.fields[field].widget.__class__.__name__ == widgets.Textarea.__name__:
                self.fields[field].widget.attrs['rows'] = '6'

    def save(self, *args, **kwargs):
        obj = super(PasswordForm, self).save(commit=False)
        obj.user = kwargs.pop('user', None)
        if 'commit' in kwargs and kwargs['commit'] is False:
            return obj
        else:
            obj.save()
            return obj

    class Meta:
        model = models.Password
        fields = ('title', 'password', 'url', 'notes')