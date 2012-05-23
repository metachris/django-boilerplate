import datetime
from pprint import pprint

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core import exceptions

import models
import tools


def home(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    # raise Http404
    return render(request, 'index.html')


def project(request, project_id):
    return HttpResponse("Project %s" % project_id)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"])
            models.UserProfile.objects.create(user=user)
            user_authenticated = auth.authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"])
            auth.login(request, user_authenticated)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
