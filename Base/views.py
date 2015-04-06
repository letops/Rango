from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Base import forms, messages as msgs, environments, queries
from Base.queries import generate_msg, GREEN, YELLOW, RED, BLUE


@login_required()
def home(request):
    return render_to_response('_rangoBase.html', context_instance=RequestContext(request))


def returnToHome():
    return HttpResponseRedirect(urlresolvers.reverse('home'))


@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(urlresolvers.reverse('login'))


def login(request):
    if request.user.is_authenticated():
        return returnToHome()
    else:
        next = username = password = ''
        if request.GET:
            next = request.GET['next']
        if request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            remember = request.POST.get('remember', None)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    if remember is not None:
                        request.session.set_expiry(72000)
                    else:
                        request.session.set_expiry(0)
                    if next == '':
                        return returnToHome()
                    else:
                        return HttpResponseRedirect(next)
                else:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        extra_tags=msgs.errors_list['title']['400'],
                        message=msgs.errors_list['body']['bad_login'],
                        fail_silently=True
                    )
            else:
                generate_msg(request, RED, msgs.errors_list['title']['400'],
                             msgs.errors_list['body']['bad_login'])
        return render_to_response(
            'login.html', {'next': next},
            context_instance=RequestContext(request),
        )


# Create your views here.
def signup(request):
    template_vars = dict()
    env = environments.Environment('signup')
    object = None
    if request.method == 'POST':
        new_object, object = push_post(request, env=env, add=True)
        # create/update has succeeded
        if new_object is not None:
            generate_msg(request, GREEN, msgs.SUCCESS, 'You have created your account.')
            return HttpResponseRedirect(urlresolvers.reverse(env.action_completed_urlname))
        else:
            generate_msg(request, YELLOW, msgs.WARNING, 'An error has occurred, please verify your signup information.')

    else:
        new_object, object = push_get(request, env=env, add=True)

    formas = {'object': object}
    return render_to_response(
        env.template,
        formas,
        RequestContext(
            request,
            template_vars
        )
    )


@login_required()
def GenericList(request, action):
    #template_vars = {'nav': get_nav_options(request), 'side': get_side_options(request)}
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
    if user.has_perm('%s.change_%s' % (environment._meta.app_label, environment.model.lower())):
        change = True
    if user.has_perm('%s.delete_%s' % (environment._meta.app_label, environment.model.lower())):
        delete = True
    return add, change, delete


@transaction.atomic()
def object_push(request, id=None, action=""):
    template_vars = dict()

    env = environments.Environment(action)
    perm_add, perm_change, perm_delete = get_permissions(request.user, env)
    object = None
    if request.method == 'POST':
        new_object, object = push_post(request, id, env, perm_add, perm_change, perm_delete)
        if new_object is not None:
            # At this point, create/update has succeeded
            if id is not None:
                generate_msg(request, GREEN) #TODO
            else:
                generate_msg(request, GREEN) #TODO
            return HttpResponseRedirect(urlresolvers.reverse(env.action_completed_urlname))
    elif request.method == 'GET':
        #Request the create/update form
        new_object, object = push_get(request, id, env, perm_add, perm_change, perm_delete)

    formas = {'object': object}
    return render_to_response(
        env.template,
        formas,
        RequestContext(
            request,
            template_vars
        )
    )


#Function executed in case that the request received
# by object_push had a POST method
def push_post(request, id=None, env=None, add=False, change=False, delete=False):
    # handle update after new data has been posted
    new_object = object_form = None
    if id is not None and change:
        #if delete:
            #Add Delete buttons

        instance = env.data_model.objects.get(pk=id)
        object_form = env.form(data=request.POST, instance=instance)

        if object_form.is_valid():
            new_object = object_form.save()

    # handle creation of new objects
    elif id is None and add:
        object_form = env.form(data=request.POST)
        if object_form.is_valid():
            new_object = object_form.save()

    else:
        generate_msg(request, RED) #TODO
    return new_object, object_form


#Function executed in case that the request received
# by object_push had a GET method
def push_get(request, id=None, env=None, add=False, change=False, delete=False):
    new_object = object = None
    if id is not None and change:
        new_object = env.data_model.objects.get(pk=id)
        object = env.form(instance=new_object)
    elif id is None and add:
        object = env.form()
    else:
        generate_msg(request, RED) #TODO

    return new_object, object