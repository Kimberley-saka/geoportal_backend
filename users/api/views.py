from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import UserModel
from .serializers import UserSerializer


class CreateUserView(APIView):
    """
    create user
    """
    def post(self, request):
        """
        __create
        """
        email = request.data.get('email')

        if UserModel.objects.filter(email=email).exists():
            return Response('detail: User with that email already exists',
                            status=status.HTTP_400_BAD_REQUEST)


class GetUserView(APIView):
    """
    get user if ther exist
    """
    def get(self, request):
        email = request.data.get('email')
        existing_user = UserModel.objects.get(email=email)
        if not existing_user:
            return Response('detail: user not found', status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(existing_user)
        return Response(serializer.data)