from . models import Property
from .serializers import PropertySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class PropertyListApi(generics.ListCreateAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    permission_classes = [IsAuthenticated,]



class PropertyDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    permission_classes = [IsAuthenticated,]
