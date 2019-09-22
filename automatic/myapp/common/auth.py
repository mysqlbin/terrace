
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# 退出登录
def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/admin/login')
