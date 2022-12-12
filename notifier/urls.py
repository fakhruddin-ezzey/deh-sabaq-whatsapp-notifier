from django.urls import path
from . import views

urlpatterns = [

    # auth view path
    path('login', views.loginview, name="login-page"),
    path('register', views.registerview, name="register-page"),
    path('verify_authtoken', views.authtokenview, name="verify-auth-token-page"),
    path('verify_success', views.authsuccessview, name="verify-auth-success-page"),

    # mumins list
    path('mumin', views.muminlist, name="mumin-list"),
    path('sabaqgroup', views.sabaqgroupsview, name="sabaq-group-list"),

]

