from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from items.models import Item
from users.models import User
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from users.api.serializer import UserSerializer


@api_view(['GET', ])
def api_detail_user_view(request):
    try:
        user = User.objects.all()   
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
