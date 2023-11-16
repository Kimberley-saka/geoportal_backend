from rest_framework.decorators import APIView
from rest_framework.response import Response

class Hello(APIView):
    """
    """
    def get(self, request):
        return Response('hello')