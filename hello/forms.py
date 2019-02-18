# -*- coding: utf-8 -*-

from django import forms

class HelloForm(forms.Form): # forms.Formというクラスを継承している
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')