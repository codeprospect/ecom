from django.shortcuts import render

# steve kindly Create your views here. And comment them every step
def homepage(request):
    return render(request, 'shop/home.html')
