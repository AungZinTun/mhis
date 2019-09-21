from rest_framework import serializers
from .models import Notify

class NotifySerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Notify
        fields="__all__"