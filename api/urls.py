from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ContactViewSet

router = routers.DefaultRouter()
router.register('contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
