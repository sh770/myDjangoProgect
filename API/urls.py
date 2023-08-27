from django.urls import path
from . import views 

urlpatterns = [
    path('' , views.getRoutes, name='index'),
    path('received-messages/', views.getReceivedMessages, name='received')
]