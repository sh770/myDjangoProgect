from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/received-messages/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of received messages'
        },
        {
            'Endpoint': '/add-message/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new message with data sent in post request'
        },
        {
            'Endpoint': '/delete-message/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting message'
        },
    ]
    # return JsonResponse(routes , safe=False)
    return Response(routes)

#all meseges
@api_view(['GET'])
def getReceivedMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many = True)
    return Response(serializer.data) 
