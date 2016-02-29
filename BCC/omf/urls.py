from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from omf import views as omf_views

router = DefaultRouter()
router.register(r'orders', omf_views.OrderViewSet)
