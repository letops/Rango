from Base import messages as msgs
from Base.views import returnToHome
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Salus import environments, queries
from Salus.queries import generate_msg, GREEN, YELLOW, RED, BLUE


@login_required()
def GenericList(request, action):
    t_vars = dict()
    env = environments.Environment(action)
    if request.method == 'GET' and request.user.has_perm('%s.list_%s' % (env.data_model._meta.app_label, env.model)):
        t_vars['headers_list'], t_vars['objects_list'], t_vars['vars'] = queries.GenericList(request, env)
    else:
        generate_msg(request, YELLOW, msgs.WARNING, msgs.NO_PERM)
        return returnToHome()

    template = env.template
    return render_to_response(
        template,
        context_instance=RequestContext(request, t_vars)
    )


def get_permissions(user, environment):
    add = change = delete = False
    if user.has_perm('%s.add_%s' % (environment.data_model._meta.app_label, environment.model.lower())):
        add = True
    if user.has_perm('%s.change_%s' % (environment.data_model._meta.app_label, environment.model.lower())):
        change = True
    if user.has_perm('%s.delete_%s' % (environment.data_model._meta.app_label, environment.model.lower())):
        delete = True
    return add, change, delete


@login_required()
@transaction.atomic()
def object_push(request, id=None, action=""):
    template_vars = dict()

    env = environments.Environment(action)
    perm_add, perm_change, perm_delete = get_permissions(request.user, env)
    instance = None
    if request.method == 'POST':
        new_instance, instance = push_post(request, id, env, perm_add, perm_change, perm_delete)
        if new_instance is not None:
            # At this point, create/update has succeeded
            if id is not None:
                generate_msg(request, GREEN, 'Success', 'Your changes were saved in the system')
            else:
                generate_msg(request, GREEN, 'Success', 'Your object was created successfully')
            return HttpResponseRedirect(urlresolvers.reverse(env.action_completed_urlname))
    elif request.method == 'GET':
        #Request the create/update form
        instance = push_get(request, id, env, perm_add, perm_change, perm_delete)

    formas = {'django_form': instance}
    return render_to_response(
        env.template,
        formas,
        RequestContext(
            request,
            template_vars
        )
    )


#Function executed in case that the request received
# by instance_push had a POST method
def push_post(request, id=None, env=None, add=False, change=False, delete=False):
    # handle update after new data has been posted
    new_instance = instance_form = None
    if id is not None and change:
        instance = env.data_model.objects.get(pk=id)
        instance_form = env.form(data=request.POST, instance=instance)

        if instance_form.is_valid():
            new_instance = instance_form.save(user=request.user)

    # handle creation of new instances
    elif id is None and add:
        instance_form = env.form(data=request.POST)
        if instance_form.is_valid():
            new_instance = instance_form.save(user=request.user)
    else:
        generate_msg(request, RED) #TODO
    return new_instance, instance_form


#Function executed in case that the request received
# by instance_push had a GET method
def push_get(request, id=None, env=None, add=False, change=False, delete=False):
    instance = None
    if id is not None and change:
        new_instance = env.data_model.objects.get(pk=id)
        instance = env.form(instance=new_instance)
    elif id is None and add:
        instance = env.form()
    else:
        generate_msg(request, RED) #TODO

    return instance