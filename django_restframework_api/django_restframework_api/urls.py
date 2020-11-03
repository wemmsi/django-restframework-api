from django.urls import include, path
from rest_framework import routers
from ropes import views

router = routers.DefaultRouter()
router.register(r'ropes', views.RopesViewSet)
router.register(r'colorschemes', views.ColorSchemesViewSet)
router.register(r'climbingropes', views.ClimbingRopesViewSet)
router.register(r'otherropes', views.OtherRopesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
