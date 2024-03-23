from django.shortcuts import render

# Create your views here.

#1 create a view for each template
#in this case the template is home.html

def home(request):
    return render(request, 'base/home.html')