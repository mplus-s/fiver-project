from djoser.serializers import UserCreatePasswordRetypeSerializer
from djoser.serializers import serializers


class CustomUserCreatePasswordRetypeSerializer(UserCreatePasswordRetypeSerializer):
    last_name = serializers.CharField(required=True, style={"input_type": "text"})
    first_name = serializers.CharField(required=True, style={"input_type": "text"})
    