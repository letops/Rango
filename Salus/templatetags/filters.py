from django import template

register = template.Library()


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
