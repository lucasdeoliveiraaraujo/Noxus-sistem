from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.


def novolaboratorio(request):
    return render(request, 'noxusapp/novolaboratorio.html')

def addLaboratorio(request):
    json_data = json.loads(request.body)
    return HttpResponse("json:"+json_data)