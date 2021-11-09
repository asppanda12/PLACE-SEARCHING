from django.shortcuts import render
from django.http import HttpResponse
import http.client, urllib.parse
import json
import requests
import ipaddress
import requests
import json
from requests.structures import CaseInsensitiveDict
import urllib.request
import math

# Create your views here.
def index(request):
    return render(request, "home.html")


def resturant(request):
    ip=(requests.get('https://api64.ipify.org').text)
    # print(ip)
    res=urllib.request.urlopen("http://ipwhois.app/json/"+ip).read()
    json_data=json.loads(res)
    lat=json_data['latitude']
    lng=json_data['longitude']
    range=20000
    res=urllib.request.urlopen("https://api.geoapify.com/v2/places?categories=catering.restaurant&filter=circle:"+str(lng)+","+str(lat)+","+str(range)+"&bias=proximity:"+str(lng)+","+str(lat)+"&limit=50&apiKey=465ea6e31b314c27b12db64eb5fa2589").read()
    json_data1=json.loads(res)
    lng1=json_data1["features"][0]["properties"]["lon"]
    lat1=json_data1["features"][0]["properties"]["lat"]
    # print(json_data1["features"][0])
    # print("{}  {} {}  {}".format(lat,lng,lng1,lat1))
    def haversine(lat1, lon1, lat2, lon2):
        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0
        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0
        a = (pow(math.sin(dLat / 2), 2) +
        pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2))
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        return rad * c

    u=json_data1["features"]
    length = len(json_data)
    p=0 
    pupils_dictionary = {}
    for x in u:
       new_key =p
       if(new_key>4):
           break
       lng1=x["properties"]["lon"]
       lat1=x["properties"]["lat"]
       name=(x['properties']['name'])
       address=(x['properties']['address_line1']+" "+x['properties']['address_line2'])
       distance=float("{:.2f}".format(haversine(lat, lng, lat1, lng1)))
       
       list=[name,address,distance]
       pupils_dictionary[new_key]=list
       p=p+1
    strp="WELCOME TO SEARCH OF RESTUARANT"
    print(pupils_dictionary)
    return render(request,'resturant.html',{'pupils_dictionary':pupils_dictionary,'heade':strp})

def police(request):
    ip=(requests.get('https://api64.ipify.org').text)
    # print(ip)
    res=urllib.request.urlopen("http://ipwhois.app/json/"+ip).read()
    json_data=json.loads(res)
    lat=json_data['latitude']
    lng=json_data['longitude']
    range=20000
    res=urllib.request.urlopen("https://api.geoapify.com/v2/places?categories=service.police&filter=circle:"+str(lng)+","+str(lat)+","+str(range)+"&bias=proximity:"+str(lng)+","+str(lat)+"&limit=62&apiKey=465ea6e31b314c27b12db64eb5fa2589").read()
    json_data1=json.loads(res)
    lng1=json_data1["features"][0]["properties"]["lon"]
    lat1=json_data1["features"][0]["properties"]["lat"]
    # print(json_data1["features"][0])
    # print("{}  {} {}  {}".format(lat,lng,lng1,lat1))
    def haversine(lat1, lon1, lat2, lon2):
        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0
        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0
        a = (pow(math.sin(dLat / 2), 2) +
        pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2))
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        return rad * c

    u=json_data1["features"]
    length = len(json_data)
    p=0 
    pupils_dictionary = {}
    for x in u:
       new_key =p
       if(new_key>4):
           break
       lng1=x["properties"]["lon"]
       lat1=x["properties"]["lat"]
       name=(x['properties']['name'])
       address=(x['properties']['address_line1']+" "+x['properties']['address_line2'])
       distance=float("{:.2f}".format(haversine(lat, lng, lat1, lng1)))
       
       list=[name,address,distance]
       pupils_dictionary[new_key]=list
       p=p+1
    strp="WELCOME TO SEARCH OF POLICE STATION"
    print(pupils_dictionary)
    return render(request,'police.html',{'pupils_dictionary':pupils_dictionary,'heade':strp})
    
def hospitals(request):
    ip=(requests.get('https://api64.ipify.org').text)
    # print(ip)
    res=urllib.request.urlopen("http://ipwhois.app/json/"+ip).read()
    json_data=json.loads(res)
    lat=json_data['latitude']
    lng=json_data['longitude']
    range=20000
    res=urllib.request.urlopen("https://api.geoapify.com/v2/places?categories=healthcare.hospital&filter=circle:"+str(lng)+","+str(lat)+","+str(range)+"&bias=proximity:86.2029579,22.8015194&limit=62&apiKey=465ea6e31b314c27b12db64eb5fa2589").read()
    json_data1=json.loads(res)
    lng1=json_data1["features"][0]["properties"]["lon"]
    lat1=json_data1["features"][0]["properties"]["lat"]
    # print(json_data1["features"][0])
    # print("{}  {} {}  {}".format(lat,lng,lng1,lat1))
    def haversine(lat1, lon1, lat2, lon2):
        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0
        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0
        a = (pow(math.sin(dLat / 2), 2) +
        pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2))
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        return rad * c

    u=json_data1["features"]
    length = len(json_data)
    p=0 
    pupils_dictionary = {}
    for x in u:
       new_key =p
       if(new_key>4):
           break
       lng1=x["properties"]["lon"]
       lat1=x["properties"]["lat"]
       name=(x['properties']['name'])
       address=(x['properties']['address_line1']+" "+x['properties']['address_line2'])
       distance=float("{:.2f}".format(haversine(lat, lng, lat1, lng1)))
       
       list=[name,address,distance]
       pupils_dictionary[new_key]=list
       p=p+1
    strp="WELCOME TO SEARCH OF HOSPITALS"
    print(pupils_dictionary)
    return render(request,'hospitals.html',{'pupils_dictionary':pupils_dictionary,'heade':strp})
        
def tourist(request):
    ip=(requests.get('https://api64.ipify.org').text)
    # print(ip)
    res=urllib.request.urlopen("http://ipwhois.app/json/"+ip).read()
    json_data=json.loads(res)
    lat=json_data['latitude']
    lng=json_data['longitude']
    range=20000
    res=urllib.request.urlopen("https://api.geoapify.com/v2/places?categories=tourism&filter=circle:"+str(lng)+","+str(lat)+","+str(range)+"&bias=proximity:"+str(lng)+","+str(lat)+"&limit=62&apiKey=465ea6e31b314c27b12db64eb5fa2589").read()
    json_data1=json.loads(res)
    lng1=json_data1["features"][0]["properties"]["lon"]
    lat1=json_data1["features"][0]["properties"]["lat"]
    # print(json_data1["features"][0])
    # print("{}  {} {}  {}".format(lat,lng,lng1,lat1))
    def haversine(lat1, lon1, lat2, lon2):
        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0
        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0
        a = (pow(math.sin(dLat / 2), 2) +
        pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2))
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        return rad * c

    u=json_data1["features"]
    length = len(json_data)
    p=0 
    pupils_dictionary = {}
    for x in u:
       new_key =p
       if(new_key>4):
           break
       lng1=x["properties"]["lon"]
       lat1=x["properties"]["lat"]
       name=(x['properties']['name'])
       address=(x['properties']['address_line1']+" "+x['properties']['address_line2'])
       distance=float("{:.2f}".format(haversine(lat, lng, lat1, lng1)))
       
       list=[name,address,distance]
       pupils_dictionary[new_key]=list
       p=p+1
    strp="WELCOME TO SEARCH OF TOURIST PLACES"
    print(pupils_dictionary)
    return render(request,'tourist.html',{'pupils_dictionary':pupils_dictionary,'heade':strp})