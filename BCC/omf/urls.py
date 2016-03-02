from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from omf import views as omf_views

router = DefaultRouter()
router.register(r'promises', omf_views.PromiseViewSet)
router.register(r'orderstatus', omf_views.OrderStatusViewSet)
router.register(r'milestones', omf_views.MilestoneViewSet)
router.register(r'predecessors', omf_views.OrderPredecessorViewSet)
router.register(r'deliveries', omf_views.DeliveryViewSet)
router.register(r'deliverables', omf_views.DeliverableViewSet)
router.register(r'lineitems', omf_views.OrderLineItemViewSet)
router.register(r'orders', omf_views.OrderViewSet)
