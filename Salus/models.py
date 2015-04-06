from django.db import models
from Base.models import RangoUser
from Salus import modelsConfig as mC


# Create your models here.
class Password(models.Model):
    """
    Represents a username and password together with several other fields
    """
    title = models.CharField(max_length=mC.password_title_length,
                             verbose_name='Name')
    username = models.ForeignKey(RangoUser, related_name="passwords", blank=False, null=False,
                                 verbose_name='User')
    password = models.CharField(max_length=mC.password_password_length,
                                verbose_name='Password')
    url = models.URLField(max_length=mC.password_url_length, blank=True,
                          verbose_name='Site URL')
    notes = models.TextField(
        max_length=mC.password_notes_length,
        blank=True,
        verbose_name='Password extra notes')
    created_at = models.DateTimeField(auto_now_add=True, editable=False,
                                      verbose_name='Date and time at which it was created')
    updated_at = models.DateTimeField(auto_now=True, editable=False,
                                      verbose_name='Date and time at which it was last updated')
    
    def __unicode__(self):
        return self.title