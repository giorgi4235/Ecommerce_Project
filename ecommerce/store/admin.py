from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(PcPart)
admin.site.register(Specs)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

