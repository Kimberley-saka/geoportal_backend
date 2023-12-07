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

        if email is None or not isinstance(email, str):
            return Response('Invalid email', status=status.HTTP_400_BAD_REQUEST)
        if UserModel.objects.filter(email=email).exists():
            return Response('detail: User with that email already exists',
                            status=status.HTTP_400_BAD_REQUEST)
        
         
        new_user_data = {'email': email, **request.data}
        new_user = UserSerializer(data=new_user_data)
        new_user = UserSerializer(data=new_user_data)
        
        if new_user.is_valid(raise_exception=True):
            new_user.save()
        
        return Response(new_user.data)
        


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