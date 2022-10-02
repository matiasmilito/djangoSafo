from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import Products, User, Orders, Order_Detail


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class OrdersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "dni", "legajo", "phone", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            dni=validated_data['dni'],
            legajo=validated_data['legajo'],
            phone=validated_data['phone'],
            password=validated_data['password']
        )
        return user


class OrdersSerializer(serializers.ModelSerializer):
    user_id = RegisterSerializer(source='user', read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


