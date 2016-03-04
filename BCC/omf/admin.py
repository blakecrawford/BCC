from django.contrib import admin

from .models import OrderStatus
from .models import Promise
from .models import Order
from .models import OrderLineItem
from .models import Deliverable
from .models import Delivery
from .models import OrderPredecessor
from .models import OrderPredecessorType
from .models import Milestone

# Register your models here.


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    extra = 1
    show_change_link = True

    verbose_name = "Order Line Item"
    verbose_name_plural = "Order Line Items"

    fields=('get_id', 'state','headline','notes',)
    readonly_fields = ('get_id','state', 'headline',)

    def get_id(self, obj):
        return obj.id
    get_id.short_description = 'Line Item ID'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class DeliverableInline(admin.TabularInline):
    model = Deliverable
    extra = 1
    show_change_link = True

    verbose_name = 'Deliverable'
    verbose_name_plural = 'Deliverables'

    fields = ('get_id', 'headline',)
    readonly_fields = ('get_id', 'headline',)

    def get_id(self, obj):
        return obj.id
    get_id.short_description = 'Deliverable ID'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class DeliveryInline(admin.TabularInline):
    model = Delivery
    extra = 1
    show_change_link = True

    verbose_name = 'Delivery'
    verbose_name_plural = 'Deliveries'

    fields = ('get_id', 'headline',)
    readonly_fields = ('get_id', 'headline')

    def get_id(self, obj):
        return obj.id
    get_id.short_description = 'Delivery ID'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class OrderPredecessorInline(admin.TabularInline):
    model = OrderPredecessor
    fk_name = 'order'
    extra = 1
    show_change_link = True

    verbose_name = 'Order Predecessor'
    verbose_name_plural = 'Order Predecessors'

    fields = ('order', 'predecessor')

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class MilestoneInline(admin.TabularInline):
    model = Milestone
    extra = 1
    show_change_link = True

    verbose_name = 'Milestone'
    verbose_name_plural = 'Milestones'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Promise)
class PromiseAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        MilestoneInline,
        OrderPredecessorInline,
        OrderLineItemInline,
    ]

    list_display = ('get_id', 'to', 'order_for','creator',)

    def get_id(self, obj):
        return obj.id
    get_id.short_description = 'Order ID'


@admin.register(OrderPredecessor)
class OrderPredecessorAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderPredecessorType)
class OrderPredecessorTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderLineItem)
class OrderLineItemAdmin(admin.ModelAdmin):
    inlines = [
        DeliverableInline,
    ]

    list_display = ('get_id', 'state', 'order', 'headline',)

    def get_id(self, obj):
        return obj.id
    get_id.short_description = 'Line Item ID'


@admin.register(Deliverable)
class DeliverableAdmin(admin.ModelAdmin):
    inlines = [
        DeliveryInline,
    ]

    list_display = ('get_lineitem_id', 'get_id', 'headline',)

    def get_lineitem_id(self, obj):
        return obj.line_item.id
    get_lineitem_id.short_description = 'Line Item ID'

    def get_id(self, obj):
        return obj.id
    get_id.short_description = 'Deliverable ID'


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('get_deliverable_id', 'get_id', 'headline',)

    def get_id(self, obj):
        return obj.id
    get_id.short_description = 'Delivery ID'

    def get_deliverable_id(self, obj):
        return obj.deliverable.id
    get_deliverable_id.short_description = 'Deliverable ID'


