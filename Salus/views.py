#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def dummy(request):
    template_vars = dict()
    template = "_rangoBase.html"
    return render_to_response(
        template,
        context_instance=RequestContext(request, template_vars)
    )
