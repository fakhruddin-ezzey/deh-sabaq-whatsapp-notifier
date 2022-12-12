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



# homepage and mumin views

def muminlist(request):
    return render(request, 'mumins/muminlist.html')

def sabaqgroupsview(request):
    return render(request, 'mumins/sabaqgroup.html')