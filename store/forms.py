from django import forms
from .models import OrderItem
from .models import Customer
from .models import Product
from .models import StoreWarehouse
from .models import ShippingAddress
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

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['customer', 'order', 'address', 'city', 'state', 'zipcode']

        widgets = {
            'customer': forms.HiddenInput(),  # Hide the customer field if you want to set it automatically
            'order': forms.HiddenInput(),     # Hide the order field if you want to set it automatically
        }