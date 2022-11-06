# the phone number tracker : 
import phonenumbers 
from test import number 
from phonenumbers import geocoder 
from phonenumbers import carrier 
c= phonenumbers.parse(number, 'CH') # CH stands for country and History 
print(geocoder.descrption_for_number(c, 'en'))
service=  phonenumbers.parse(number , "RO")
print(carrier.name_for_number(service , 'en'))


