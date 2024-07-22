# from django.db import models

# class Subscription(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     vibhag = models.CharField(max_length=100)
#     jila = models.CharField(max_length=100)
#     nagar_khand = models.CharField(max_length=100)
#     baiti_mandal = models.CharField(max_length=100)
#     subscriber_name = models.CharField(max_length=100)
#     subscriber_phone = models.CharField(max_length=15)
#     subscriber_email = models.EmailField()
#     post_office_name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.subscriber_name



from rest_framework import serializers
# from .models import Subscription

class SubscriptionSerializer(serializers.Serializer):
    #     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     vibhag = models.CharField(max_length=100)
#     jila = models.CharField(max_length=100)
#     nagar_khand = models.CharField(max_length=100)
#     baiti_mandal = models.CharField(max_length=100)
#     subscriber_name = models.CharField(max_length=100)
#     subscriber_phone = models.CharField(max_length=15)
#     subscriber_email = models.EmailField()
#     post_office_name = models.CharField(max_length=100)
    amount = serializers.CharField(required=True)
    vibhag = serializers.CharField(required=True)
    nagar_khand = serializers.CharField(required=True)
    
    jila = serializers.CharField(required=True)
    pincode = serializers.CharField(required=True)
    referred_person = serializers.CharField(required=True)
    referred_person_phone = serializers.CharField(required=True)
    subscription_type = serializers.CharField(required=True)
    
    baiti_mandal = serializers.CharField(required=True)
    subscriber_name = serializers.CharField(required=True)
    subscriber_phone = serializers.CharField(required=True)
    subscriber_email = serializers.CharField(required=True)
    subscriber_address = serializers.CharField(required=True)
    post_office_name = serializers.CharField(required=True)
    _ = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    
    class Meta:
        fields = '__all__'





