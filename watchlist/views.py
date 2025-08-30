from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Watchlist
from companies.models import Company

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_watchlist(request):
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    companies = watchlist.companies.all()
    data = [{"symbol": c.symbol, "company_name": c.company_name} for c in companies]
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_watchlist(request):
    symbol = request.data.get('symbol')
    if not symbol:
        return Response({"error": "Symbol is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        company = Company.objects.get(symbol=symbol)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

    watchlist, _ = Watchlist.objects.get_or_create(user=request.user)
    watchlist.companies.add(company)
    return Response({"detail": f"{symbol} added to watchlist"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_from_watchlist(request):
    symbol = request.data.get('symbol')
    if not symbol:
        return Response({"error": "Symbol is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        company = Company.objects.get(symbol=symbol)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

    watchlist = Watchlist.objects.get(user=request.user)
    if company not in watchlist.companies.all():
        return Response({"error": "Company not in watchlist"}, status=status.HTTP_400_BAD_REQUEST)

    watchlist.companies.remove(company)
    return Response({"detail": f"{symbol} removed from watchlist"}, status=status.HTTP_200_OK)