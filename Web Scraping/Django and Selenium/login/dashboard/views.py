from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import EmployeeDetails

def index(request):
    resultdisplay=EmployeeDetails.objects.all()
    return render(request, 'dashboard/index.html', {'items': resultdisplay})

