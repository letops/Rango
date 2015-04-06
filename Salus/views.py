from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from Salus.forms import PasswordForm


def dummy(request):
    template_vars = dict()
    template = "_rangoBase.html"
    return render_to_response(
        template,
        context_instance=RequestContext(request, template_vars)
    )
