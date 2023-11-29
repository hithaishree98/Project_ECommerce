from django import forms
from .models import OrderItem
from .models import Customer
from .models import Product
from .models import StoreWarehouse

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'order', 'quantity']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'BrandName', 'BagType', 'AverageRating', 'InventoryQuantity']

class StoreWarehouseForm(forms.ModelForm):
    class Meta:
        model = StoreWarehouse
        fields = ['address', 'store_manager', 'salespersons', 'region_ID']