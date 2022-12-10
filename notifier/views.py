from django.shortcuts import render

# authentication views
def loginview(request):
    return render(request, 'authentication/login.html')

def registerview(request):
    return render(request, 'authentication/register.html')

def authtokenview(request):
    return render(request, 'authentication/verify_authtoken.html')

def authsuccessview(request):
    return render(request, 'authentication/verify_success.html')