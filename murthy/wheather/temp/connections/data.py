import os
from urllib import response
from django.http import JsonResponse
import pymongo
from pymongo import MongoClient
from rest_framework import status
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
def post_data(request):
    url="https://en.wikipedia.org/wiki/India"
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    count=0
    for link in soup.findAll('a'):
        if count==7:
            val=link.get('href')
            break
        count=count+1
        # print(link.get('href')
    print(val)
    flag='https://upload.wikimedia.org/wikipedia/en/4/41/'+val[5:],
    capital='New Delhi'
    largest_city=['mumbai','new delhi']
    officiallanguage=['hindi','english']
    area_total=3287263
    population=1353642280
    gdpnominal='$3.050 trillion'
    data={
        'flag_link':flag,
        'capital':capital,
        'largest_city':largest_city,
        'official_language':officiallanguage,
        'area_total':area_total,
        'population':population,
        'GDP_nominal':gdpnominal
    }
    return JsonResponse(data)