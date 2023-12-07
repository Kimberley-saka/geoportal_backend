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
            return Response({'detail: User already exists'}, status=status.HTTP_409_CONFLICT)
        
        new_user = UserSerializer(data=request.data) 
        if new_user.is_valid(raise_exception=True): #check if data passed is valid
            new_user.save()
        
        return Response(new_user.data, status=status.HTTP_201_CREATED)
            
    
    
class GetUserView(APIView):
    """
    get user if the exist
    """
    def get(self, request):
        email = request.data.get('email')
        existing_user = UserModel.objects.get(email=email)
        if not existing_user:
            return Response('detail: user not found', status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(existing_user)
        return Response(serializer.data)