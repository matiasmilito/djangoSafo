import email

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Products, User, Orders, Order_Detail
from safoBack import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


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
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
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

        # if User.objects.filter(email=email).exists():
        #     raise ValidationError("El mail ya existe")
            # si el mail ingresado por el usuario ya existe, se devuelve el mensaje "el mail ya existe"
        #
        if user is not {}:
            subject = 'Bienvenido a SAFO  no-reply'
            message = 'Hola ' + first_name + ' ' + last_name + ' Se ha registrado con exito - No responder a este mensaje.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [validated_data['email']]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        user.save()
        # si el usuario no está vacio, se envia el mail con los datos del mismo.
        return user


class OrdersSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(source='user_id', read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.user_mail = validated_data.get('user_mail', instance.user_mail)
        instance.state = validated_data.get('state', instance.state)
        mail = instance.user_mail
        orderid = instance.id
        total = instance.total_price
        if instance.state == 'A retirar':
            subject = 'Retire su orden - SAFO'
            message = 'Hola, su orden n°' + str(orderid) +' esta lista para ser retirada por la fotocopiadora. Recuerde que debe abonar $' + str(total) + ' al retirarla. Muchas gracias.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [mail]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        elif instance.state == 'En proceso':
            subject = 'Orden confirmada - SAFO'
            message = 'Hola, su orden n°' + str(orderid) + ' esta fue confirmada. Recuerde que le llegara un mail cuando este disponible para ser retirada por la fotocopiadora y debe abonar $' + str(total) + ' al retirarla. Muchas gracias.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [mail]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        instance.save()
        return instance


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


