from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    """ Home page of the web app """
    return render(request, "homepage/home.htm")

def signup_view(request):
    """ Sign up page for new users """
    return render(request, "homepage/signup.htm")

def signin_view(request):
    """ Sign in page for users """
    return render(request, "homepage/signin.htm")