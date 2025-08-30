from rest_framework import serializers
from companies.serializers import CompanySerializer
from .models import Watchlist

class WatchlistSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)
    company_ids = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )

    class Meta:
        model = Watchlist
        fields = ['companies', 'company_ids']