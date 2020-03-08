from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from .serializers import UserSerializer, ImageSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings
from .models import User
from django.contrib.auth import get_user_model
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny, ])
def signup(request):
    print('singup')
    serializer = UserSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        print('통과실패')
        password = request.data.get('password')
        user = serializer.save()
        user.set_password(password)
        user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return JsonResponse({'token': token})
    return HttpResponse(status=400)

def mypage(request, id):
    print('mypage@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(id)
    user = get_object_or_404(get_user_model(), id=id)
    print(user)
    serializer = ImageSerializer(user)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def inimage(request, id=id):
    user = get_object_or_404(get_user_model(), id=id)
    # serializer = UserSerializer(user, data= request.data)
    # serializer.save()
    image = request.FILES['file']
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(image)
    user.image = image
    user.save()
    serializer = ImageSerializer(user)
    return JsonResponse(serializer.data)

