from rest_framework import serializers
from omf.models import Promise
from omf.models import Order
from omf.models import OrderStatus
from omf.models import Milestone
from omf.models import OrderPredecessor
from omf.models import OrderLineItem
from omf.models import Deliverable
from omf.models import Delivery


class PromiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promise
        fields = ('type', 'parameters')


class OrderStatus(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(many=False, read_only=True)

    class Meta:
        model = OrderStatus
        fields = ('report_datetime', 'reporter', 'status_note', 'status_flag', 'order')


class MilestoneSerializer(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(many=False, read_only=True)

    class meta:
        model = Milestone
        fields = ('order', 'milestone', 'date_time')


class OrderPredecessorSerializer(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(many=False, read_only=False)
    predecessor = serializers.HyperlinkedRelatedField(many=False, read_only=False)
    class Meta:
        model = OrderPredecessor
        fields = ('order', 'predecessor')


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('headline',)


class DeliverableSerializer(serializers.ModelSerializer):
    deliveries = DeliverySerializer

    class Meta:
        model = Deliverable
        fields = ('headline', 'deliveries')


class OrderLineItemSerializer(serializers.ModelSerializer):
    deliverables = DeliverableSerializer

    class Meta:
        model = OrderLineItem
        fields = ('state', 'headline', 'notes', 'deliverables')


class OrderSerializer(serializers.ModelSerializer):
    line_items = OrderLineItemSerializer(many=True, read_only=False)
    milestones = MilestoneSerializer(many=True, read_only=False)
    predecessors = OrderPredecessorSerializer(many=True, read_only=False)
    to = serializers.HyperlinkedRelatedField(many=False, read_only=True)
    order_for = serializers.HyperlinkedRelatedField(many=False, read_only=True)
    parent = serializers.HyperlinkedRelatedField(many=False, read_only=True)

    class Meta:
        model = Order
        fields = ('to', 'order_for', 'creator', 'parent', 'line_items', 'milestones', 'predecessors')
