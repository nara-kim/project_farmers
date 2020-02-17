from django.shortcuts import render, get_object_or_404
from .serializers import SnsSerializer, TodoSerializer, SnsSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import SnsModel, CommentModel
from django.contrib.auth import get_user_model
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

@api_view(['POST'])
def snscreate(request):
    print('imageinfo@@@@@@@@@@@@@@@@')
    aaa = request.FILES['file']
    title = request.POST['title']
    user = request.POST['user']
    user = get_object_or_404(get_user_model(), username=user)
    img = SnsModel.objects.create(image=aaa, title=title, user=user)
    return JsonResponse({"asd":"asd"})

def snslist(request):
    sns = SnsModel.objects.all()
    if request.method == 'GET':
        serializer = SnsSerializer(sns, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def commentcreate(request,id):
    print('commentcreate')
    sns = get_object_or_404(SnsModel, id=id)
    content = request.POST['content']
    user = request.POST['user']
    user = get_object_or_404(get_user_model(), username=user)
    img = CommentModel.objects.create(content=content, sns=sns, create_user=user)
    serializer = CommentSerializer(instance=img)
    return JsonResponse(serializer.data)


@api_view(['GET','DELETE'])
def comment(request,id):
    print('??????')
    if request.method == 'GET':
        sns = get_object_or_404(SnsModel, id=id)
        comments = sns.commentmodel_set.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        print('delete')
        comment = get_object_or_404(CommentModel, id=id)
        serializer = CommentSerializer(instance=comment)
        comment.delete()
        return JsonResponse(serializer.data)