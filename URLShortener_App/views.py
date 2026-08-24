from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import URLShortenerSerializer
from .service import generate_short_url
# Create your views here.



class URLShortener(APIView):
    permission_classes = [AllowAny]

    def post(self, request,):
        pass