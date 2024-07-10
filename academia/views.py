from django.shortcuts import render
from academia.models import Academia

# Create your views here.
def index(request):
    academias = Academia.objects.all()
    return render(request, 'academia/index.html', {"cards": academias})