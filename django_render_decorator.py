from django.shortcuts import render_to_response
from django.template import RequestContext


def render(template_name):
    def outer(func):
        def inner(request, *args, **kwargs):
            return render_to_response('{0:s}.html'.format(template_name),
                func(request, *args, **kwargs),
                context_instance=RequestContext(request))
        return inner
    return outer
