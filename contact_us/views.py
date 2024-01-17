from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from .serializers import ContactUsSerializer
# Create your views here.


class ContactUsView(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    # eigula builtin variables serializer modelviewset er

    # akhon amader app er model tar akta json automatic create hoye jabe akhon urls.py a akta router banay niye CRUD operation chalano jabe