from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def retrieve_view(request):
    employees=Employee.objects.all()
    return render(request,'testapp/index.html',{"employees":employees})