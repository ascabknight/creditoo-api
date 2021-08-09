from django.urls import path, include
from rest_framework import routers
from cartera import views

router = routers.DefaultRouter()
router.register(r'personas', views.PersonaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
