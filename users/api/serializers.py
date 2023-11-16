from rest_framework.serializers import ModelSerializer
from users.models import UserModel


class UserSerializer(ModelSerializer):
    """
    serialize user model
    """
    model = UserModel

    fields = '__all__'

    extra_kwargs = {
        'password': {'write_only': True}
    }