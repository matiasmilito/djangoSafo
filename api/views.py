from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Products, Orders, Order_Detail
from api.serializers import ProductsSerializer, RegisterSerializer, MeSerializer, OrdersSerializer, \
    OrdersDetailSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        queryset = self.queryset.all()
        categoria = self.request.query_params.get('categoryId')
        id = self.request.query_params.get('id')
        if categoria is not None and id is not None:
            queryset = queryset.filter(categoryId=categoria).filter(id=id)
        elif categoria is not None:
            queryset = queryset.filter(categoryId=categoria)
        elif id is not None:
            queryset = queryset.filter(id=id)
        return queryset

    # def get_queryset(self):
    #     queryset = self.queryset.all()
    #     id = self.request.query_params.get('id')
    #     if id is not None:
    #         queryset = queryset.filter(id=id)
    #     return queryset


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()


class OrdersDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersDetailSerializer
    queryset = Order_Detail.objects.all()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    print(MeSerializer(request.user))
    return Response(MeSerializer(request.user).data, 200)


