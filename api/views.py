from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Products, Orders, Order_Detail, User
from api.serializers import ProductsSerializer, RegisterSerializer, MeSerializer, OrdersSerializer, \
    OrdersDetailSerializer, UserSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 15

class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    # pagination_class = StandardResultsSetPagination

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
    queryset = Orders.objects.order_by('date')
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = self.queryset.all()
        id = self.request.query_params.get('user_id')
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset


class OrdersDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersDetailSerializer
    queryset = Order_Detail.objects.all()

    def get_queryset(self):
        queryset = self.queryset.all()
        orderId = self.request.query_params.get('order_id')
        if orderId is not None:
            queryset = queryset.filter(order_id=orderId)
        return queryset


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = StandardResultsSetPagination


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    print(MeSerializer(request.user))
    return Response(MeSerializer(request.user).data, 200)


