from rest_framework import serializers
from pizzApp.models import pizzaInfo



class pizzaInfoSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = pizzaInfo
        fields = ['id',  'pizzatype', 'pizzasize', 'pizzatopping']
