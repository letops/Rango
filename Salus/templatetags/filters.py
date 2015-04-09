from django import template
from django.core import urlresolvers

register = template.Library()


@register.filter()
def equal_urlnames(url_path, url_name):
    return urlresolvers.resolve(url_path).url_name == url_name


@register.filter()
def geturlid(url_path):
    return urlresolvers.resolve(url_path).kwargs['id']



@register.filter()
def can_add(user, model):
    if user.is_super() or user.is_admin():
        return True
    else:
        return user.has_perm("%s.add_%s" % (model._meta.app_label, model))


@register.filter()
def can_edit(user, model):
    if user.is_super() or user.is_admin():
        return True
    else:
        return user.has_perm("%s.change_%s" % (model._meta.app_label, model))


@register.filter()
def can_delete(user, model):
    if user.is_super() or user.is_admin():
        return True
    else:
        return user.has_perm("%s.delete_%s" % (model._meta.app_label, model))


@register.filter()
def geturl(model, object):
    pass
