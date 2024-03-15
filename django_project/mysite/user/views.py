from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileForm, UserForm


# Create your views here.


def register_view(request):
    form = UserRegisterForm(request.POST)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserRegisterForm(request.POST)
            return render(request, 'user/register.html', context=context)
    else:
        form = UserRegisterForm()
        context = {'form': form}
        print('*********************get')
        return render(request, 'user/register.html', context=context)


def profile_view(request):
    u_form = UserForm(request.POST, instance=request.user)
    p_form = ProfileForm(request.POST, instance=request.user.profile)

    print('***************************')
    print(request.POST)
    print('**************************')

    if request.method == "POST":
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'user/profile.html', context=context)
