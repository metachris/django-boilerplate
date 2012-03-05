# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404


def home(request):
    return HttpResponse("Hello, world. You're at the poll index.")
    #return render_to_response('main/index.html')


def project(request, project_id):
    return HttpResponse("Project %s" % project_id)
