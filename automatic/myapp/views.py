from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.include import meta
from myapp.include import function as func
from myapp.include import sqlfilter
from myapp.form import AddForm

from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import F,Max,Sum,Value as V
from django.db.models.functions import Concat
from automatic import settings

from django.core import serializers

from myapp.common.utils.rewrite_json_encoder import RewriteJsonEncoder


import datetime,time
import json
import os


@login_required(login_url='/admin/login/')
def index(request):

    return render(request, 'index.html')


@login_required(login_url='/admin/login/')
@permission_required(perm='myapp.menu_binlog2sql', raise_exception=True)
def binlog2sql(request):

    return render(request, 'binlog2sql.html')


@login_required(login_url='/admin/login/')
@permission_required(perm='myapp.menu_pollingreport', raise_exception=True)
def polling_report(request):

    return render(request, 'polling_report.html')

@login_required(login_url='/admin/login/')
@permission_required(perm='myapp.menu_instance', raise_exception=True)
def instance(request):

    return render(request, 'instance.html')

@login_required(login_url='/admin/login/')
@permission_required(perm='myapp.menu_slowquery', raise_exception=True)
def slowquery(request):

    return render(request, 'showquery.html')


