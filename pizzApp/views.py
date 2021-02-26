from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import pizzaInfo
# Create your views here.



def pizzainfo(request):

    if request.method == "POST":
        pizzatype = request.POST['pizzatype']
        pizzasize = request.POST['pizzasize']
        pizzatopping = request.POST['pizzatopping']
       
        print(pizzatype, pizzasize, pizzatopping)
        if len(pizzasize) < 2 or len(pizzatopping) < 3 :
            messages.error(request, 'Please fill the information correctly')
        else:
            if pizzaInfo.objects.filter(pizzasize=request.POST['pizzasize'],pizzatype=request.POST['pizzatype']).exists():
                PizzaInfo = pizzaInfo(pizzatype=pizzatype, pizzasize=pizzasize,
                                pizzatopping=pizzatopping)
                PizzaInfo.save()
                messages.success(
                    request, 'Your information has been recorded. Thankyou  ')
            else:
                messages.error(request, 'This size or type  is not available ')

    return render(request, 'pizzainfo.html')

    
    
