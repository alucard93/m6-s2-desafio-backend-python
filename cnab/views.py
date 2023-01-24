from django.shortcuts import render


# Create your views here.
def cnab(request):
    return render(request, 'home.html')