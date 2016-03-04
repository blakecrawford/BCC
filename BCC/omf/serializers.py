from rest_framework import serializers
from omf.models import Promise
from omf.models import Order
from omf.models import OrderStatus
from omf.models import Milestone
from omf.models import OrderPredecessor
from omf.models import OrderPredecessorType
from omf.models import OrderLineItem
from omf.models import Deliverable
from omf.models import Delivery


class PromiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promise
        fields = ('type', 'parameters')


class OrderStatusSerializer(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(view_name='order-detail', many=False, read_only=True)

    class Meta:
        model = OrderStatus
        fields = ('report_datetime', 'reporter', 'status_note', 'status_flag', 'order')


class MilestoneSerializer(serializers.ModelSerializer):
    #order = serializers.HyperlinkedRelatedField(view_name='order-detail', many=False, read_only=True)

    class Meta:
        model = Milestone
        fields = ('milestone', 'date_time')

class OrderPredecessorTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderPredecessorType
        fields = ('name',)


class OrderPredecessorSerializer(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(view_name='order-detail', many=False, read_only=True)
    predecessor = serializers.HyperlinkedRelatedField(view_name='order-detail', many=False, read_only=True)

    class Meta:
        model = OrderPredecessor
        fields = ('order', 'predecessor')


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ('headline',)


class DeliverableSerializer(serializers.ModelSerializer):
    deliveries = DeliverySerializer(many=True, read_only=True)

    class Meta:
        model = Deliverable
        fields = ('headline', 'deliveries',)


class OrderLineItemSerializer(serializers.ModelSerializer):
    deliverables = DeliverableSerializer(many=True, read_only=True)

    class Meta:
        model = OrderLineItem
        fields = ('state', 'headline', 'notes', 'deliverables',)


class OrderSerializer(serializers.ModelSerializer):

    line_items = OrderLineItemSerializer(many=True, read_only=True)
    milestones = MilestoneSerializer(many=True, read_only=True)
    predecessors = OrderPredecessorSerializer(many=True, read_only=True)
    to = serializers.HyperlinkedRelatedField(view_name='endpoint-detail', many=False, read_only=True)
    order_for = serializers.HyperlinkedRelatedField(view_name='endpoint-detail', many=False, read_only=True)
    parent = serializers.HyperlinkedRelatedField(view_name='order-detail', many=False, read_only=True)
    statuses = OrderStatusSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('to', 'order_for', 'creator', 'statuses','parent', 'line_items', 'milestones', 'predecessors')
