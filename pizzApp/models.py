from django.db import models
from djchoices import DjangoChoices, ChoiceItem

# Create your models here.


class pizzaInfo(models.Model):
    # Choices
    PIZZA_TYPE = (
        ("R", "Regular"),
        ("S", "Square"),
    
    )
    # Fields
    ## "id" is autogenrated in django if we don't use of primary key.
    pizzatype = models.CharField(max_length=20, choices=PIZZA_TYPE)
    pizzasize = models.CharField(max_length=20)
    pizzatopping = models.CharField(max_length=20)
    
    class Meta:  
        db_table = "Pizza_Info"

