from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        # pyrefly: ignore [bad-override-mutable-attribute]
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        ]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        # pyrefly: ignore [bad-override-mutable-attribute]
        fields = ["id", "username", "email", "first_name", "last_name"]
