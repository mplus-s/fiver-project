from rest_framework import serializers
from .models import Product , Cart ,CartItem
from categories.models import Category
from users.models import User
from rest_framework import serializers
from drf_base64.fields import Base64ImageField

class ProductSerializer(serializers.ModelSerializer):
    photo1 = Base64ImageField()
    photo2 = Base64ImageField()
    photo3 = Base64ImageField()
    photo4 = Base64ImageField()

    category = serializers.SlugRelatedField(read_only=False, queryset=Category.objects.all(), slug_field="name")
    added_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        exclude = ("id", "added_at",)
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
    
    def validate_cart(self, value):
        if value == 0:
            return None
        return value
    
    def validate(self, validated_data):
        cart = validated_data['cart']
        customer = validated_data['customer']
        if cart == None:
            cart = Cart.objects.create(customer=customer)
            validated_data['cart'] = cart
        return validated_data

class CartitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
    