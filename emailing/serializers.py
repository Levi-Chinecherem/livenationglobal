
# emailing/serializers.py
from rest_framework import serializers
from .models import EmailInfo

class EmailInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailInfo
        fields = '__all__'
