from rest_framework import generics, permissions
from .models import Company
from .serializers import CompanySerializer
from django_filters import rest_framework as filters

class CompanyFilter(filters.FilterSet):
    company_name = filters.CharFilter(lookup_expr='icontains')
    symbol = filters.CharFilter(lookup_expr='icontains')
    scripcode = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['company_name', 'symbol', 'scripcode']

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CompanyFilter
    pagination_class = None  # or keep pagination