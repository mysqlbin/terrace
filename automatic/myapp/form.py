# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(
        required=True,
        max_length=25,
        label="用户名:",
        error_messages={'required': u'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }
        ),
    )

    password = forms.CharField(
    required=True,
    max_length=25,
    label="密码:",
    error_messages={'required': u'请输入密码'},
    widget=forms.PasswordInput(
        attrs={
            'placeholder': u"密码",
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()



class AddForm (forms.Form):
    a = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 15}))


# class Captcha(forms.Form):
#     mycaptcha = CaptchaField(label="验证码:",)


