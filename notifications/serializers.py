from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['sender']

class BulkNotificationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    notifications = NotificationSerializer(many=True)
