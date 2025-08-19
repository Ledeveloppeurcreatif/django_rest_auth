from django.urls import path,include
from rest_framework import routers
from .views import CategorieViewSet, HelloWorldView, MissionViewSet


router = routers.DefaultRouter()
router.register('Mission', MissionViewSet)
router.register('Categorie', CategorieViewSet)
#router.register('Signalement', SignalementViewSet)

urlpatterns = [
    path('hello', HelloWorldView.as_view()),
    path('', include(router.urls)),
    
]

