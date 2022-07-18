from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django.http import Http404
from django.shortcuts import render

class MyAccountAdapter(DefaultAccountAdapter):
    
    def get_login_redirect_url(self, request):
        try:
            path = "/{grupo}/"
            return path.format(grupo=request.user.grupo)
        except path.DoesNotExist:
            raise Http404('Url não existe ou não permitida!')
        return render(request, 'Error/404.html')