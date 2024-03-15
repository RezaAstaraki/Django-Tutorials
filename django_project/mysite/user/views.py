from django.shortcuts import render, redirect
from .forms import UserRegisterForm


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

    return render(request, 'user/profile.html')
