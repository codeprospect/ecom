from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('homepage')
    else:
        form = UserRegisterForm()

    return render(request, 'users/registration.html', {'form': form})

#login view

@login_required
def profile(request):
    return render(request, 'users/profile.html')
#we are doing this for practice
