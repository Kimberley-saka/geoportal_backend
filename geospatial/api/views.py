from rest_framework.decorators import APIView
from rest_framework.response import Response

class getGeoData(APIView):
    def get(self, request):
        return Response('some data')