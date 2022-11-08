from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import ProductsViewSet, OrdersViewSet, OrdersDetailViewSet, RegisterView, me, UserViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'orderdetail', OrdersDetailViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('me/', me)
]