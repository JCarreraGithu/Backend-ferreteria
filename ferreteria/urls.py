from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompraViewSet, EmpleadoViewSet, ProductoViewSet, ProveedorViewSet, VentaViewSet
from .views import ClienteViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'producto', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'compras', CompraViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
