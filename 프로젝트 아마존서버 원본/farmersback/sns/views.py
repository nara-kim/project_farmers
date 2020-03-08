from django.shortcuts import render, get_object_or_404
from .serializers import SnsSerializer, TodoSerializer, SnsSerializer, SnsCreateSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import SnsModel, CommentModel
from django.contrib.auth import get_user_model
from accounts.models import User
from accounts.serializers import ImageSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])  # JWT 방식으로 인증 및 허가 하겠다.
def sns_create(request):
    serializer = SnsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)

    return HttpResponse(status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
@authentication_classes([JSONWebTokenAuthentication])  # JWT 방식으로 인증 및 허가 하겠다.
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)

    return HttpResponse(status=400)

@api_view(['POST'])

def snscreate(request):
    aaa = request.FILES['file']
    title = request.POST['title']
    user = request.POST['user']
    username = request.POST['user']
    user = get_object_or_404(get_user_model(), username=user)
    nickname= user.nickname
    img = SnsModel.objects.create(image=aaa, title=title, user=user, username=username, nickname=nickname)
    user.sns_count += 1
    user.save()
    return JsonResponse({"asd":"asd"})



def snslist(request):
    sns = SnsModel.objects.all().order_by('-id')

    if request.method == 'GET':
        serializer = SnsSerializer(sns, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def commentcreate(request,id):
    sns = get_object_or_404(SnsModel, id=id)
    content = request.POST['content']
    user = request.POST['user']
    username = request.POST['user']
    user = get_object_or_404(get_user_model(), username=user)
    img = CommentModel.objects.create(content=content, sns=sns, create_user=user, username=username)
    user.comment_count += 1
    user.save()
    serializer = CommentSerializer(instance=img)
    return JsonResponse(serializer.data)


@api_view(['GET','DELETE'])
def comment(request,id):
    if request.method == 'GET':
        sns = get_object_or_404(SnsModel, id=id)
        comments = sns.commentmodel_set.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        comment = get_object_or_404(CommentModel, id=id)
        user = get_object_or_404(get_user_model(), username=comment.username)
        user.comment_count -= 1
        user.save()
        serializer = CommentSerializer(instance=comment)
        comment.delete()
        return JsonResponse(serializer.data)

@api_view(['DELETE'])
def snsdelete(request, id):
    sns = get_object_or_404(SnsModel, id=id)
    user = get_object_or_404(get_user_model(), nickname=sns.nickname)
    user.sns_count += -1
    user.save()
    serializer = SnsSerializer(instance=sns)
    sns.delete()
    return JsonResponse(serializer.data)

def getranker(request):
    snsrankers = User.objects.all().order_by('-sns_count')[:5]
    
    sns_rankers = ['',0,'','',0,'','',0,'','',0,'','',0,'',]
    
    idx = 0
    for ranker in snsrankers:
        sns_rankers[idx] = ranker.nickname
        sns_rankers[idx+1] = ranker.sns_count
        origin = ranker.username

        origin = origin[0:2] + '****'
        sns_rankers[idx+2] = origin
        idx += 3

    commentrankers = User.objects.all().order_by('-comment_count')[:5]
    comment_rankers = ['',0,'','',0,'','',0,'','',0,'','',0,'',]
    idx = 0
    for ranker in commentrankers:
        comment_rankers[idx] = ranker.nickname
        comment_rankers[idx+1] = ranker.comment_count
        origin = ranker.username

        origin = origin[0:2] + '****'
        comment_rankers[idx+2] = origin
        idx += 3
    
    rankerdata = {
        'sns1_name':sns_rankers[0],'sns1_count':sns_rankers[1],'sns1_id':sns_rankers[2],
        'sns2_name':sns_rankers[3],'sns2_count':sns_rankers[4],'sns2_id':sns_rankers[5],
        'sns3_name':sns_rankers[6],'sns3_count':sns_rankers[7],'sns3_id':sns_rankers[8],
        'sns4_name':sns_rankers[9],'sns4_count':sns_rankers[10],'sns4_id':sns_rankers[11],
        'sns5_name':sns_rankers[12],'sns5_count':sns_rankers[13],'sns5_id':sns_rankers[14],
        'comment1_name':comment_rankers[0],'comment1_count':comment_rankers[1],'comment1_id':comment_rankers[2],
        'comment2_name':comment_rankers[3],'comment2_count':comment_rankers[4],'comment2_id':comment_rankers[5],
        'comment3_name':comment_rankers[6],'comment3_count':comment_rankers[7],'comment3_id':comment_rankers[8],
        'comment4_name':comment_rankers[9],'comment4_count':comment_rankers[10],'comment4_id':comment_rankers[11],
        'comment5_name':comment_rankers[12],'comment5_count':comment_rankers[13],'comment5_id':comment_rankers[14],
    }
    return JsonResponse(rankerdata)


def getuser(request,id):
    sns = get_object_or_404(SnsModel, id=id)
    user = get_object_or_404(get_user_model(), nickname=sns.nickname)
    serializer = ImageSerializer(user)
    return JsonResponse(serializer.data)