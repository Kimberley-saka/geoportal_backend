from rest_framework.serializers import ModelSerializer
from users.models import UserModel


class UserSerializer(ModelSerializer):
    """
    serialize user model
    """
    class Meta:
        model = UserModel

        fields = ['email', 'first_name', 'last_name', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        """
        Create user with hashed password
        """
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
