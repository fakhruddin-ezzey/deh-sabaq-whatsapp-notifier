from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from .serializers import DEHAdminSerializer

from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .auth.authsec import DEHAdminRegister
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate, logout

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


# authentication APIs

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
            is_created = False
            api_status_code = HTTP_500_INTERNAL_SERVER_ERROR
        
        return Response({'is_created':is_created,'status':api_status_code})



class VerifyDEHAdmin(APIView):

    def put(self, request, format=None):
        is_verified = True
        api_status_code = HTTP_200_OK

        data = request.data

        try:
            print(data.get("tokenkey"))
            user_instance = Token.objects.get(key=data.get('tokenkey')).user
            print(user_instance.is_active)
            user_model = get_object_or_404(User, pk=user_instance.id)
            print(user_model.id)
            print("processed model")
            activate_serial_data = {'is_active':True}
            patch_serializer_to_activate = DEHAdminSerializer(user_model, data=activate_serial_data, partial=True)
            print("serialized patch")
            if patch_serializer_to_activate.is_valid():
                print("saving")
                patch_serializer_to_activate.save()
                pass
                print("saved")
            else:
                error_list = [patch_serializer_to_activate.errors[error][0] for error in patch_serializer_to_activate.errors]
                print(error_list)
                is_verified = False
                api_status_code = HTTP_500_INTERNAL_SERVER_ERROR
        except Exception as e:
            pass

        return Response({'is_verified':is_verified,'api_status_code':api_status_code})


class ValidateDEHAdmin(APIView):

    def post(self, request, format=None):
        print(request.user.is_authenticated)
        is_validated = True
        api_status_code = HTTP_200_OK

        data = request.data
        print(data)

        authenticating_email = data.get('authenticate_email')
        authenticating_password = data.get('authenticate_password')

        if request.user.is_authenticated:
            pass
        else:
            try:
                existing_user = User.objects.get(email=authenticating_email)
                user_model_validated = authenticate(username=existing_user.username, password=authenticating_password)
                if user_model_validated is not None and user_model_validated.is_active:
                    print("authed")
                    login(request, user_model_validated)
                    print("authed complete")
                else:
                    print("not authed")
                    is_validated = False
                    api_status_code = HTTP_500_INTERNAL_SERVER_ERROR    
            except Exception as e:
                print(type(e).__name__,'========>', e.args)
                is_validated = False
                api_status_code = HTTP_500_INTERNAL_SERVER_ERROR
            
        return Response({'is_validated':is_validated, 'api_status_code':api_status_code})


# homepage and mumin views

def muminlist(request):
    return render(request, 'mumins/muminlist.html')

def sabaqgroupsview(request):
    return render(request, 'mumins/sabaqgroup.html')