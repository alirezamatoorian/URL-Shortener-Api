from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import URLSerializer
from .service import generate_short_url
from .models import URL
# Create your views here.



class URLShortenerView(APIView):
    permission_classes = [AllowAny]

    def post(self, request,):
        serializer = URLSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        short_url = generate_short_url()
        original_url = serializer.validated_data["original_url"]
        URL.objects.create(original_url=original_url,short_url=short_url)
        return Response(URLSerializer.data,status=status.HTTP_201_CREATED)
