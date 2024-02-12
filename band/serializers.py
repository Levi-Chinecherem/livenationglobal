# band/serializers.py
from rest_framework import serializers
from .models import Band, MembershipType, PaymentType, CommonFields, Membership
from accounts.serializers import UserSerializer  # Assuming you have a UserSerializer in the accounts app

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'

class MembershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipType
        fields = '__all__'

class CommonFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonFields
        fields = '__all__'

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'

class MembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    band = BandSerializer(read_only=True)
    common_fields = CommonFieldsSerializer()
    payment_type = PaymentTypeSerializer() 
    
    class Meta:
        model = Membership
        fields = '__all__'
