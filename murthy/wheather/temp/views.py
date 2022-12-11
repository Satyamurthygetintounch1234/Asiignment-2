from django.shortcuts import render
from rest_framework.views import APIView
from temp.connections.data import post_data
class data(APIView):
    def get(self,request,format=None):
        return post_data(request)
# Create your views here.
