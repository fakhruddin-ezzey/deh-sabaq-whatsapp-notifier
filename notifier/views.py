from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from .serializers import DEHAdminSerializer

from .auth.authsec import DEHAdminRegister

# authentication views
class LoginDEHAdminView(TemplateView):

    template_name = 'authentication/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RegisterDEHAdminView(TemplateView):

    template_name = 'authentication/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VerifyDEHAdminTokenView(TemplateView):

    template_name = 'authentication/verify_authtoken.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VerifyDEHAdminSuccessView(TemplateView):

    template_name = 'authentication/verify_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RegisterDEHAdmin(APIView):

    def post(self, request, format=None):

        is_created = True
        api_status_code = HTTP_200_OK

        draft_data = request.data.copy()
        deh_admin_data_morpher = DEHAdminRegister(draft_data)
        draft_data = deh_admin_data_morpher.return_morphed_request()
        deh_admin_serializer = DEHAdminSerializer(data=draft_data)
        if deh_admin_serializer.is_valid():
            deh_admin_serializer.save()
        else:
            print(draft_data)
            error_list = [deh_admin_serializer.errors[error][0] for error in deh_admin_serializer.errors]
            print(error_list)
            is_created = False
            api_status_code = HTTP_500_INTERNAL_SERVER_ERROR
        
        return Response({'is_created':is_created,'status':api_status_code})


# homepage and mumin views

def muminlist(request):
    return render(request, 'mumins/muminlist.html')

def sabaqgroupsview(request):
    return render(request, 'mumins/sabaqgroup.html')