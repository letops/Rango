from Base import messages as msgs
from Base.views import returnToHome
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from Salus import environments, queries
from Salus.queries import generate_msg, GREEN, YELLOW, RED, BLUE


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