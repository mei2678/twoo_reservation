from rest_framework.views import APIView
from rest_framework.response import Response
from booking_management.models import Reservations
from .serializers import VisitHistorySerializer


class VisitHistoryView(APIView):
    def get(self, request, user_id):
        visits = Reservations.objects.filter(status='completed', user_id=user_id)
        serializer = VisitHistorySerializer(visits, many=True)
        return Response(serializer.data)