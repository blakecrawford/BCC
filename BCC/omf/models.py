from django.shortcuts import get_object_or_404
from django.db import models
from django_enumfield import enum
from epd.models import Endpoint


class OrderStates(enum.Enum):
    PENDING = 0
    INPROGRESS = 1
    COMPLETE = 2

    labels = {
        PENDING: 'Pending',
        INPROGRESS: 'In Progress',
        COMPLETE: 'Complete'
    }


class StatusFlags(enum.Enum):
    NORMAL = 0
    WARNING = 1
    ERROR = 2

    labels = {
        NORMAL: 'Normal',
        WARNING: 'Warning',
        ERROR: 'Error'
    }


class LineItemStates(enum.Enum):
    AVAILABLE = 0
    ENABLED = 1
    ACTIVE = 2
    COMPLETED = 3

    labels = {
        AVAILABLE: 'Available',
        ENABLED: 'Enabled',
        ACTIVE: 'Active',
        COMPLETED: 'Completed'
    }


class Promise(models.Model):
    type = models.CharField(max_length=256, null=False)
    parameters = models.TextField(null=False)

    def __unicode__(self):
        return u"Promise :: "

    class Meta:
        verbose_name = "Promise"
        verbose_name_plural = "Promises"


class OrderPredecessorType(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Predecessor Type"
        verbose_name_plural = "Predecessor Types"


class Order(models.Model):
    to = models.ForeignKey(Endpoint, related_name='order_to')
    order_for = models.ForeignKey(Endpoint, related_name='order_for')
    creator = models.CharField(max_length=256, null=False)
    parent = models.ForeignKey("self", null=True, blank=True, related_name='parent_order')

    def __unicode__(self):
        return u"Order To " + \
                self.to.name + \
                u" For " + \
                self.order_for.name

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderStatus(models.Model):
    report_datetime = models.DateTimeField(auto_now_add=True)
    reporter = models.CharField(max_length=256)
    status_note = models.TextField(null=True)
    status_flag = enum.EnumField(StatusFlags, default=StatusFlags.NORMAL)
    order = models.ForeignKey(Order, null=True, related_name='statuses')

    def __unicode__(self):
        return u"Order Status :: "

    class Meta:
        verbose_name = "Order Status"
        verbose_name_plural = "Order Statuses"


class Milestone(models.Model):
    order = models.ForeignKey(Order, null=True, related_name='milestones')
    milestone = enum.EnumField(OrderStates, default=OrderStates.PENDING)
    date_time = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return u'Milestone :: ' + \
                str(self.milestone)

    class Meta:
        verbose_name = "Milestone"
        verbose_name_plural = "Milestones"


class OrderPredecessor(models.Model):
    order = models.ForeignKey(Order, related_name='order')
    predecessor = models.ForeignKey(Order, related_name='predecessors')
    predecessor_type = models.ForeignKey(OrderPredecessorType, null=True, blank=True)

    def __unicode__(self):
        return u"Order :: " + \
                str(self.order.id) + \
                u" Must Be Preceded By :: " + \
                str(self.predecessor.id)

    class Meta:
        verbose_name = "Order Predecessor"
        verbose_name_plural = "Order Predecessors"


class OrderLineItem(models.Model):
    state = enum.EnumField(LineItemStates, default=LineItemStates.AVAILABLE)
    headline = models.CharField(max_length=256, null=False)
    notes = models.TextField(null=True)
    order = models.ForeignKey(Order, null=True, related_name='line_items')

    def __unicode__(self):
        return u"Line item ID " + \
                str(self.id) + \
                u' For Order ID ' + \
                str(self.order.id)

    class Meta:
        verbose_name = "Order Line Item"
        verbose_name_plural = "Order Line Items"


class Deliverable(models.Model):
    headline = models.CharField(max_length=256, null=False)
    line_item = models.ForeignKey(OrderLineItem, null=True, related_name='deliverables')

    def __unicode__(self):
        return u"Deliverable ID " + \
                str(self.id) + \
                u" For Line Item ID " + \
                str(self.line_item.id)

    class Meta:
        verbose_name = "Deliverable"
        verbose_name_plural = "Deliverables"


class Delivery(models.Model):
    headline = models.CharField(max_length=256, null=False)
    deliverable = models.ForeignKey(Deliverable, null=True, related_name='deliveries')

    def __unicode__(self):
        return u"Delivery ID " + \
                str(self.id) + \
                u" For Deliverable ID " + \
                str(self.deliverable.id)

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"


