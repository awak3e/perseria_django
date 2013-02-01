from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from home.models import BreakdownCover


class LoginForm(forms.Form):
    lusername = forms.CharField(max_length=20)
    lpassword = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    rusername = forms.CharField(max_length=20)
    rpassword = forms.CharField(widget=forms.PasswordInput())
    rpassword_confirm = forms.CharField(widget=forms.PasswordInput())
    remail = forms.EmailField()

def index(request):
    return render(request, 'index.html')

def cover(request):
    cover_list = BreakdownCover.objects.get(user=request.user)
    return render(request, 'cover.html', { 'coverlist' : cover_list, })

def auth(request):
    form = LoginForm()
    form2 = RegisterForm()
    
    if request.method == 'POST':
        if 'submitLogin' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                lusername = form.cleaned_data['lusername']
                lpassword = form.cleaned_data['lpassword']
                
                user = authenticate(username=lusername, password=lpassword)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect("/")
                else:
                    form.errors['__all__'] = form.error_class(["Your username or password is incorrect"])
        
        elif 'submitRegister' in request.POST:
            form2 = RegisterForm(request.POST)
            if form2.is_valid():
                rusername = form2.cleaned_data['rusername']
                rpassword = form2.cleaned_data['rpassword']
                rpassword_confirm = form2.cleaned_data['rpassword_confirm']
                remail = form2.cleaned_data['remail']
                
                if (rpassword == rpassword_confirm):
                    if User.objects.filter(username=rusername).count() == 0:
                        User.objects.create_user(rusername, remail, rpassword)
                        user = authenticate(username=rusername, password=rpassword)
                        login(request, user)
                        return HttpResponseRedirect("/")
                    else:
                        form2.errors['__all__'] = form.error_class(["Username already exists"])
                else:
                    form2.errors['__all__'] = form.error_class(["The passwords do not match"])
            
                
    return render(request, 'auth.html', {'form' : form, 'form2' : form2,})
    
def signout(request):
    logout(request)
    return HttpResponseRedirect("/")