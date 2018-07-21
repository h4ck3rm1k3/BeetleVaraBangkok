from .models import SourceSite
from rest_framework import serializers

class SourceSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceSite
        fields = ('id','STATUS', 'name',  'website')
