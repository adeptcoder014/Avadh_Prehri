from django.shortcuts import render

# Create your views here.
from rest_framework import status as stus
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .models import Subscription
from .serializer import SubscriptionSerializer
from .queries import *
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime

@api_view(['POST'])
# ... (authentication and permission decorators)

def create_subscription(request):
    try:
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.data['amount']
            vibhag = serializer.data['vibhag']
            nagar_khand = serializer.data['nagar_khand']
            baiti_mandal = serializer.data['baiti_mandal']
            subscriber_name = serializer.data['subscriber_name']
            subscriber_phone = serializer.data['subscriber_phone']
            subscriber_email = serializer.data['subscriber_email']
            subscriber_address = serializer.data['subscriber_address']
            post_office_name = serializer.data['post_office_name']
            
            jila = serializer.data['jila']
            pincode = serializer.data['pincode']
            referred_person = serializer.data['referred_person']
            referred_person_phone = serializer.data['referred_person_phone']
            subscription_type = serializer.data['subscription_type']
      

       
       
       

            data = {
                'subscriber_name': subscriber_name,  
                'subscriber_phone': subscriber_phone, 
                'subscriber_email': subscriber_email,  
                'subscriptionDate': datetime.datetime.now(),
                'subscriptionType': 'active',  
                'subscriptionStatus': 'active',  
                'subscriberAddress': subscriber_address, 
                'amount': amount,
                'vibhag': vibhag,
                
                
                'nagar_khand': nagar_khand,
                'baiti_mandal': baiti_mandal,
                'post_office_name': post_office_name,  
                # 'UpdatedAt': datetime.datetime.now(),
                
                'jila': jila,
                'pincode': pincode,
                'referred_person': referred_person,
                'referred_person_phone': referred_person_phone,
                'subscription_type': subscription_type,
            }

            insert_product =insert_subscriber(list(data.values()))

            if insert_product:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': "",
                    'message': 'Data Inserted Successfully',
                }
                return Response(json_data, status=stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Failed',
                    'data': '',
                    'message': 'Data Insertion Failed',
                }
                return Response(json_data, status=stus.HTTP_200_OK)

        else:
            json_data = {
                'status_code': 300,
                'status': 'Failed',
                'data': serializer.errors,
                'message': 'Please Enter All Fields'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)

    except Exception as e:
        json_data = {
            'status_code': 400,
            'status': 'Failed',
            'Reason': e,
            'Remark': 'Landed in Exception',
        }
        raise APIException(json_data)





@api_view(['POST'])
# @authentication_classes((TokenAuthentication,))
# @permission_classes((IsAuthenticated,))
def Get_subscribers(request):
    """
    API endpoint to retrieve all subscribers.
    """
    try:
        subscribers = get_subscriber()  # Fetch all subscribers from the database
        return Response(subscribers, status=stus.HTTP_200_OK)  # Return serialized data
    except Exception as e:
        # Handle any exceptions that might occur during retrieval
        return Response({'error': str(e)}, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)
