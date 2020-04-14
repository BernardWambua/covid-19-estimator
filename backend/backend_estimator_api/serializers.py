from rest_framework import serializers
from .models import Logs


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ['http_method', 'request_path',
                  'request_status', 'request_time']
