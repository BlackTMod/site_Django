from django.shortcuts import render
from django.http import HttpResponse
#home page views

# Create your views here.
def homePage(request):
    message = "Or contact us"
    return render(request, 'home.html', {'msg': message})
    '''template def name (request):
        return render(request, 'htmlfile.html')
        '''