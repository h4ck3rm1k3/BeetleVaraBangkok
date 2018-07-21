from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SourceSiteSerializer
from .models import SourceSite

class SourceSiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows source sites to be viewed or edited.
    """
    queryset = SourceSite.objects.all()
    serializer_class = SourceSiteSerializer
