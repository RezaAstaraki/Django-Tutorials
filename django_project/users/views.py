from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm
# from django.contrib.auth.views import LoginView

from django.contrib.auth import authenticate

# Create your views here.

form = UserRegisterForm()


def user_register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # print(request.POST)
        # print(form)
        context = {'active': 'register', 'form': form}
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            messages.success(request, f"""Account Created For {
                             user_name} successfully""")

            form.save()
            return redirect(reverse('blog-home'))
    else:
        form = UserRegisterForm()
        context = {'active': 'register', 'form': form}

    return render(request,
                  'users/user_register.html', context=context)


def logout_view(request):
    logout(request)
    view_ = render(request, 'users/logout.html')
    return view_


@login_required
def profile_view(request):
    if request.user:
        user_update_form = UserForm(instance=request.user)
        user_profile_update_form = UserProfileForm(
            instance=request.user.profile)
    else:
        user_update_form = UserForm()
        user_profile_update_form = UserProfileForm()
    context = {
        'u_form': user_update_form,
        'p_form': user_profile_update_form,
    }

    if request.method == "POST":
        if user_profile_update_form.is_valid() and user_update_form.is_valid():
            messages.success(request, f"""Your Account Updated Successfully {
                             request.user}""")
            user_profile_update_form.save()
            user_update_form.save()
            return redirect(reverse('blog-home'))
            return render(request, 'users/profile.html', context=context)

    return render(request, 'users/profile.html', context=context)
