from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from .models import Sender, Notification
from .serializers import  BulkNotificationSerializer

# Create your views here.
def home(request):
    return JsonResponse({

       'project': 'Bulk Notifications API',
       'version': '1.0.0',
       'status': 'running',
       'available_endpoints': [
           {
               'method': 'POST',
                'url': '/api/notifications/bulk/',
                'description': 'Create bulk notifications and a  sender with a single request.'
            
            },
            {
                'method': 'GET',
                'url': '/admin/',
                'description': 'Access the Django admin panel to manage senders and notifications.'
            }
       ]   
    })
class BulkNotificationView(APIView):
    def post(self,request):
        
        serializer = BulkNotificationSerializer(data=request.data)
        if serializer.is_valid():

            with transaction.atomic():

              validated = serializer.validated_data

              sender = Sender.objects.create(
                 name=validated['name'],
                 email=validated['email']
                )

            notifications = []

            for notification in validated['notifications']:

                    notifications.append(

                      Notification(
                        title=notification['title'],
                        message=notification['message'],
                        channel=notification['channel'],
                        sender=sender
                    )
                )
            Notification.objects.bulk_create(notifications)

            return Response(
                    {
                        'message': 'Bulk notifications created successfully.',
                        'sender_id': sender.id,
                        'notifications_created': len(notifications)

                    },
                    status=status.HTTP_201_CREATED
                )
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             