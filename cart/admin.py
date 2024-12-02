from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CartItem, PurchasedItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')

@admin.register(PurchasedItem)
class PurchasedItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'purchase_date')
