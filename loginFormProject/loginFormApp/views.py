from django.shortcuts import render
from . import forms

# Create your views here.
def userLogin(request):
    loginForm = forms.Login()
    if request.method == 'POST':
        loginForm = forms.Login(request.POST)
        if loginForm.is_valid():
            print("Form is valid")
            print("User Name : "+loginForm.cleaned_data['userName'])
            print("Password : "+loginForm.cleaned_data['password'])
    return render(request, 'loginFormApp/loginForm.html', {'form':loginForm})
