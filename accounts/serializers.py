from rest_framework import serializers

from accounts.models import Account
from accounts.utils import check_email, clearbit_info


class CreateAccountSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={"input_type": "password"}, required=True)

    class Meta:
        model = Account
        fields = ("email", "first_name", "last_name", "password",)

    def validate(self, attrs):
        if not check_email(attrs['email']):
            raise serializers.ValidationError("Email is not valid")
        return attrs

    def create(self, validated_data):
        acc = Account.objects.create(
            email=validated_data.get("email"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
        )
        acc.set_password(validated_data.get('password'))
        acc.save()
        return acc


class AccountSerializer(serializers.ModelSerializer):
    clear_bit = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ("email", "first_name", "last_name", "clear_bit")

    def get_clear_bit(self, obj):
        return clearbit_info(obj.email)
