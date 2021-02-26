from django.urls import path , include
from .API import viewsets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pizzaInfo', viewsets.pizzaInfoViewset , basename='pizzainfo')


urlpatterns = [

    path('', include(router.urls))
]