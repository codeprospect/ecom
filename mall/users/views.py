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

# def login(request):
#     if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect('homepage')
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	else:
# 		messages.error(request,"Invalid username or password.")
#
#     form = AuthenticationForm()
#     return render(request, 'users/login.html')
#
#
# #logout view
# def logout(request):
#     return render(request, 'users/logout.html')
