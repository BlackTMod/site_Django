from django.shortcuts import render
from django.http import HttpResponse
#Error page views

# Create your views here.
def errorPage(request):
    message = "Or contact us"
    return render(request, 'error404.html', {'msg': message})
    '''template def name (request):
        return render(request, 'htmlfile.html')
        '''