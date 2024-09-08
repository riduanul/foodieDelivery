from django.contrib import admin
from user.models import Restaurant, CustomUser


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'address']

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'role', 'restaurant']



admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(CustomUser, UserAdmin)