from rest_framework.decorators import APIView, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.models import UserModel
from .serializers import UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """custom claim jwt"""
    @classmethod
    def get_token(cls, user):
        """
        __summary__
        """
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    """
    serialize
    """
    serializer_class = MyTokenObtainPairSerializer

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
    @permission_classes([IsAuthenticated])
    def get(self, request):
        """
        __get authenticated user
        """
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        