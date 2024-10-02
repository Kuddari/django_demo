from django.shortcuts import render

# Create your views here.
# myapp/views.py

def home(request):
    return render(request, 'home.html')
