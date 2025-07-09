"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path, include
# se importa las vistas de la aplicación
from administrativo import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'edificios', views.EdificioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
