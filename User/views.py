from multiprocessing import AuthenticationError
from django import urls
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from braces. views import GroupRequiredMixin
from requests import request
from User.models import User
from Produtos.models import Pipeline


class HomePage(TemplateView):
    template_name = 'home.html'


class HomeEQUIPE(GroupRequiredMixin, TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = User.objects.all()
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prod'] = Pipeline.objects.all()
        return context
    
    group_required = u'EQUIPE'
    template_name = 'EQUIPE.html'


class HomeFCB(GroupRequiredMixin, TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prod'] = Pipeline.objects.filter(empresa='FCB')     
        return context

    group_required = u'FCB'
    template_name = 'FCB.html'


class HomeGALERIA(GroupRequiredMixin, TemplateView):
   
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prod'] = Pipeline.objects.filter(empresa='GALERIA')
        return context

    template_name = 'GALERIA.html'
    group_required = u'GALERIA'
         


class HomeDPZT(GroupRequiredMixin, TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prod'] = Pipeline.objects.filter(empresa='DPZT')
        return context   

    group_required = u'DPZT'
    template_name = 'DPZT.html'
