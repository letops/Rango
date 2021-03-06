from Base import messages as msgs
from Base.queries import generate_msg, GREEN, YELLOW, RED, BLUE
from Salus import serializers, models
import sys, simplejson


def PasswordsListQuery(request, env):
    try:
        headers = ('Title', 'Password')
        objects = env.data_model.objects.filter(user=request.user)
        serializer = serializers.SimplePasswordSerializer(objects, many=True)
        return headers, simplejson.loads(simplejson.dumps(serializer.data)), {'list_name': 'Passwords',
                                                                              'data_model': env.data_model,
                                                                              'add': 'add_password',
                                                                              'change': 'change_password',
                                                                              'delete': 'delete_password'}

    except:
        print("Unexpected error:", sys.exc_info())
        generate_msg(request, RED, msgs.ERROR, msgs.TICKET)
        return None, None, None


def GenericList(request, environment):
    return environment.function(request, environment)


def delete_password(id):
    try:
        password = models.Password.objects.get(id=id)
        password.delete()
        return True
    except:
        return False
