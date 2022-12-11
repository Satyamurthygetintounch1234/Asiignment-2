from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from temp.views import data
urlpatterns=[
    path('india/',csrf_exempt(data.as_view())),
]