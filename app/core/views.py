from django.shortcuts import render
from .models import Name, Address
# Create your views here.

def index(request):
    name = Name.objects.all()
    address = Address.objects.all()
    context = {
        'name': name,
        'address': address

    }
    return render(request, template_name='index.html', context=context)
