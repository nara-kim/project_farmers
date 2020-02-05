from django.shortcuts import render, get_object_or_404
from .serializers import SnsSerializer, TodoSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])  # JWT 방식으로 인증 및 허가 하겠다.
def sns_create(request):
    print('tltltlt')
    serializer = SnsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)

    return HttpResponse(status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
@authentication_classes([JSONWebTokenAuthentication])  # JWT 방식으로 인증 및 허가 하겠다.
def todo_create(request):
    print('ggg')
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)

    return HttpResponse(status=400)
