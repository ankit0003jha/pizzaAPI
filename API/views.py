from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from pizzApp.models import pizzaInfo
from .serializers import pizzaInfoSerializer 
from django.http import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
# Create your views here.


##  use this function based view when you dont want to use modelviewset view  




@api_view(['GET', 'POST', 'DELETE'])
def pizza_Info(request):
    if request.method == 'GET':
        pizza = pizzaInfo.objects.all()
        pizzaInfo_serializer = pizzaInfoSerializer(pizza, many=True)
        return JsonResponse(pizzaInfo_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        pizzaInfo_data = JSONParser().parse(request)
        pizzaInfo_serializer = pizzaInfoSerializer(data=pizzaInfo_data)
        if pizzaInfo_serializer.is_valid():
            pizzaInfo_serializer.save()
            return JsonResponse(pizzaInfo_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(pizzaInfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = pizzaInfo.objects.all().delete()
        return JsonResponse({'message': '{} pizzaInfo were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)