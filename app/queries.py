
from django.db import models
# Create your models here.
from django.db import connection, transaction, connections
import sys
import os
import datetime
import re
import time
import random
from datetime import datetime
from .helper import *
from django.core.mail import EmailMultiAlternatives

# Helper Quries


def dictfetchall(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def replace_null_with_empty_string_many(result):
    for dictionary in result:
        for i in dictionary:
            if dictionary[i] == 'NULL' or dictionary[i] == None or dictionary[i] == 'None' or dictionary[i] == 'null':
                dictionary[i] = ''
            elif type(dictionary[i]) == int:
                dictionary[i] = str(dictionary[i])
    return result


def replace_null_with_empty_string(dictionary):
    for i in dictionary:
        if dictionary[i] == 'NULL' or dictionary[i] == None or dictionary[i] == 'None' or dictionary[i] == 'null':
            dictionary[i] = ''
        elif type(dictionary[i]) == int:
            dictionary[i] = str(dictionary[i])
    return dictionary






def insert_subscriber(data):
    with connections['default'].cursor() as cursor:
        resp = cursor.execute("""
            INSERT INTO `AvadhPrehriSubscribers` (
                `subscriberName`,
                `subscriberNumber`,
                `subscriberEmail`,
                `subscriptionDate`,
                `subscriptionType`,
                `subscriptionStatus`,
                `subscriberAddress`,
                `amount`,
                `vibhag`,
                `nagarKhand`,
                `baitiMandal`,
                `POName`,
                jila,
                pincode,
                referred_person,
                referred_person_phone,
                subscription_type
                
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s
            );
        """, data)
        resp = cursor.lastrowid
        return resp


def get_subscriber():
    with connections['default'].cursor() as cursor:
        resp = cursor.execute(
            """SELECT * FROM AvadhPrehriSubscribers""")
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp