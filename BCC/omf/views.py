from rest_framework import viewsets
import omf.serializers
import omf.models

# class ChannelViewSet(viewsets.ModelViewSet):
#     queryset = refdata.models.Channel.objects.all()
#     serializer_class = refdata.serializers.ChannelSerializer


class PromiseViewSet(viewsets.ModelViewSet):
    queryset = omf.models.Promise.objects.all()
    serializer_class = omf.serializers.PromiseSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = omf.models.OrderStatus.objects.all()
    serializer_class = omf.serializers.OrderStatus


class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = omf.models.Milestone.objects.all()
    serializer_class = omf.serializers.MilestoneSerializer


class OrderPredecessorViewSet(viewsets.ModelViewSet):
    queryset = omf.models.OrderPredecessor.objects.all()
    serializer_class = omf.serializers.OrderPredecessorSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = omf.models.Delivery.objects.all()
    serializer_class = omf.serializers.DeliverySerializer


class DeliverableViewSet(viewsets.ModelViewSet):
    queryset = omf.models.Deliverable.objects.all()
    serializer_class = omf.serializers.DeliverableSerializer


class OrderLineItemViewSet(viewsets.ModelViewSet):
    queryset = omf.models.OrderLineItem.objects.all()
    serializer_class = omf.serializers.OrderLineItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = omf.models.Order.objects.all()
    serializer_class = omf.serializers.OrderSerializer

