from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'restaurant', 'payment_method',  'total_price', 'created_at')
    list_filter = ('payment_method', 'restaurant')
    search_fields = ('user__username', 'restaurant__name')
  



admin.site.register(Order, OrderAdmin)