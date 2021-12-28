from rest_framework import serializers

from main.models import BaseModel


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ('name', 'qty', 'distance')
