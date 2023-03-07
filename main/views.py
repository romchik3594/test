from django.shortcuts import render
from main.models import IoT
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    db = IoT.objects.get(id=1)
    return render(request,'main/index.html',{'db':db})
def somepage(request):
    return render(request,'main/somepage.html')
@csrf_exempt
def update(request):
    db = IoT.objects.get(id=1)
    return HttpResponse(db.gas)