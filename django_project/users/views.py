from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.shortcuts import redirect
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def register_view(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
        else:
            form = UserRegisterForm(request.POST)
    else:   
        form = UserRegisterForm()
    context = {'form':form}
    return render(request,'users/register.html',context=context)



# def login_view(request):
    # form = AuthenticationForm()
    # context = {'form':form}
    # form.confirm_login_allowed()
    # return render(request,'users/login.html',context=context)

# from django.contrib.auth import login
# from django.contrib.





