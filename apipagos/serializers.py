from rest_framework import serializers
from .models import Service,PaymentUser,ExproredPaument

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = '__all__',

    
class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = '__all__'
        read_only_fields = ('payment_date','expiration_date',)


class ExproredPaumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExproredPaument
        fields = '__all__'
        read_only_fields = '__all__',

