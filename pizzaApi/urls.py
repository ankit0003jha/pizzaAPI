"""pizzaApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from .router import router
from API import views
#url = 'http://127.0.0.1:8000/api/pizzaInfo/'
urlpatterns = [
    path('', include('pizzApp.urls')),
    path('admin/', admin.site.urls),
    path('api/' , include(router.urls)),
    
    ## pk = primary key
    ## here primary key is 'id'
    ## used when make use of class based views
    #url(r'^api/create/$', views.pizza_Info, name='pizza_Info'),
    #url(r'^api/(?P<pk>\d+)/update/$', views.pizza_Info, name='pizza_Info'),
    #url(r'^api/(?P<pk>\d+)/delete/$', views.pizza_Info, name='pizza_Info'),

#</pk></pk>
]
