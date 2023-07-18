from django.shortcuts import render

# Create your views here.

def usdf(request):
    d={'data':'Hai HarShad'}
    return render(request, 'usdf.html',d)