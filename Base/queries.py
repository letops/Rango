from Base import models, serializers, messages as msgs
from django.contrib import messages
import sys, simplejson

GREEN = 'green'
BLUE = 'blue'
YELLOW = 'yellow'
RED = 'red'


def generate_msg(request, state=None, title=None, body=None):
    mtype = None
    if state == GREEN:
        mtype = messages.SUCCESS
    elif state == BLUE:
        mtype = messages.INFO
    elif state == YELLOW:
        mtype = messages.WARNING
    elif state == RED:
        mtype = messages.ERROR

    messages.add_message(
        request,
        mtype,
        extra_tags=title,
        message=body,
        fail_silently=True
    )


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


def UsersListQuery(request, env):
    try:
        headers = ('Username', 'Email', 'Avatar')
        if request.user.is_admin() or request.user.is_super():
            objects = env.data_model.objects.all()
        else:
            objects = env.data_model.objects.filter(id=request.user.id)
        serializer = serializers.SimpleUserSerializer(objects, many=True)
        return headers, simplejson.loads(simplejson.dumps(serializer.data)), {'list_name': 'Users',
                                                                              'data_model': env.data_model,
                                                                              'add': 'add_user',
                                                                              'change': 'change_user',
                                                                              'delete': 'delete_user'}

    except:
        print("Unexpected error:", sys.exc_info())
        generate_msg(request, RED, msgs.ERROR, msgs.TICKET)
        return None, None, None


def GenericList(request, environment):
    return environment.function(request, environment)