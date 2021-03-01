from API.viewsets import pizzaInfoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pizzaInfo', pizzaInfoViewset)
