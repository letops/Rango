from Base import models


def actions_in_list(user, model, data_model):
    view = edit = delete = False
    if user.has_perm('Main.query_%s' % model):
        view = True
    if user.has_perm('Main.change_%s' % model):
        edit = True
    if user.has_perm('Main.delete_%s' % model):
        delete = True

    actions = {
        'query': {'active': view, 'url': ''},
        'change': {'active': edit, 'url': ''},
        'delete': {'active': delete, 'url': ''},
    }
    return actions


def UsersList(request, environment):
    objects = models.RangoUser.objects.all()
    serializer = environment.serializer(objects, many=True)
    fields_list = environment.fields
    return fields_list, serializer.data