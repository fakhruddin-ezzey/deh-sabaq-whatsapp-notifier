from django.urls import path
from . import views

urlpatterns = [

    # auth view path
    path('login', views.LoginDEHAdminView.as_view(), name="login-page"),
    path('register', views.RegisterDEHAdminView.as_view(), name="register-page"),
    path('verify_authtoken', views.VerifyDEHAdminTokenView.as_view(), name="verify-auth-token-page"),
    path('verify_success', views.VerifyDEHAdminSuccessView.as_view(), name="verify-auth-success-page"),

    #auth apis
    path('register_deh_admin',views.RegisterDEHAdmin.as_view(), name="register-deh-admin"),

    # mumins list
    path('mumin', views.muminlist, name="mumin-list"),
    path('sabaqgroup', views.sabaqgroupsview, name="sabaq-group-list"),

]

