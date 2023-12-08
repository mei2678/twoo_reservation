from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer

class CustomUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)