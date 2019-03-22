from django.utils import timezone
import os
import googlemaps
from googlemaps import convert
import datetime
import json
import time
from haversine import haversine

from django.conf import settings
import juspayp3 as Juspay

import requests
import dealer.models as m


def address_to_lat_long(address):
    # bound_lat_lng =  {"southwest":[23.63936, 68.14712], "northeast":[28.20453, 97.34466]}
    # BOUNDS_INDIA = convert.bounds(bound_lat_lng)
    # try:
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    geocode_result = gmaps.geocode(address)
        # geocode_pin = gmaps.geocode(pincode)
        # add_lat = geocode_result[0]["geometry"]["location"]["lat"]
        # add_lng = geocode_result[0]["geometry"]["location"]["lng"]
        # pin_lat = geocode_pin[0]["geometry"]["location"]["lat"]
        # pin_lng = geocode_pin[0]["geometry"]["location"]["lng"]
        # add = (float(add_lat), float(add_lng))
        # pin = (float(pin_lat), float(pin_lng))
        # distance = haversine(add, pin)
    #     if distance < 10:
    #     else:
    #         location = 0
    # except:
    #     location = 0
    location = geocode_result[0]["geometry"]["location"]
    return location


def sms(to, message):
    from twilio.rest import Client
    account = "ACXXXXXXXXXXXXXXXXX"
    token = "YYYYYYYYYYYYYYYYYY"
    client = Client(account, token)