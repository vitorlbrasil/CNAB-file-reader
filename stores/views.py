from django.shortcuts import render
from rest_framework.generics import ListAPIView

from stores.models import Store
from .serializers import StoreSerializer


class StoreView(ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
