from django.shortcuts import render, get_object_or_404
from .serializers import HelpSerializers
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from .models import HelpModel
# Create your views here.

@api_view(['POST'])
def help_create(request):
    help_select = request.POST['help_select']
    title = request.POST['title']
    location1 = request.POST['location1']
    location2 = request.POST['location2']
    help_date = request.POST['help_date']
    people = request.POST['people']
    content = request.POST['content']
    user = request.POST['user']
    username = request.POST['user']

    user = get_object_or_404(get_user_model(),username=user)
    helpmodel = HelpModel.objects.create(help_select=help_select, title=title, location1=location1, location2=location2, help_date=help_date, people=people, content=content, user=user, username=username)
    return JsonResponse({"pasd":"asd"})

def gethelp(request):
    helpmodel = HelpModel.objects.all()
    serializer = HelpSerializers(helpmodel, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def locationhelp(request):
    location1 = request.POST['location1']
    location2 = request.POST['location2']
    helpmodel = HelpModel.objects.filter(location1=location1, location2=location2)
    serializer = HelpSerializers(helpmodel, many=True)
    return JsonResponse(serializer.data, safe=False)

def helpdetail(request, id):
    helpmodel = get_object_or_404(HelpModel, id=id)
    serializer = HelpSerializers(helpmodel)
    return JsonResponse(serializer.data)

@api_view(['DELETE'])
def helpdelete(request, id):
    helpmodel = get_object_or_404(HelpModel, id=id)
    serializer = HelpSerializers(instance=helpmodel)
    helpmodel.delete()
    return JsonResponse(serializer.data)