from rest_framework import viewsets
from pizzApp.models import pizzaInfo
from . import serializers
from .serializers import pizzaInfoSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class pizzainfoViewPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3      ###pagination on the basis of no. of items

class pizzaInfoViewset(viewsets.ModelViewSet):
    queryset = pizzaInfo.objects.all()
    serializer_class = pizzaInfoSerializer
    filter_backends = (DjangoFilterBackend , SearchFilter , OrderingFilter)
    filter_fields = ['pizzatype', 'pizzasize']
    search_fields = ['id',  'pizzatype', 'pizzasize', 'pizzatopping']
    pagination_class = pizzainfoViewPagination
    ordering_fields = ['id']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]




