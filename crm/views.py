from django.shortcuts import render_to_response
from django.template import RequestContext


# for each model, add, change and delete permission are created,
# use a "@permission_required('type_model')" imply registred user.

# from django.contrib.auth.decorators import permission_required
# @permission_required('add_exemple')
def greetings(request, name=None):
    return render_to_response("crm/greetings.html",
                              {
                                  "name": name or "no_name"
                              },
                              context_instance=RequestContext(request)
                             )

# Create your views here.
