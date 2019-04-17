# -*- coding: utf-8 -*-
from django import forms

class AddForm (forms.Form):
    a = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 15}))
