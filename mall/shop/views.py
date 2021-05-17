from django.shortcuts import render

# steve kindly Create your views here.
def homepage(request):
    return render(request, 'shop/home.html')
