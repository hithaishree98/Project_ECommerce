from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    customer_type = models.TextField(max_length=200, null=True, default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
    BrandName = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    BagType = models.CharField(max_length=200, null=True)
    AverageRating = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    InventoryQuantity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    store_id = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Sproduct(models.Model):
    name = models.CharField(max_length=200, null=True)
    image1 = models.ImageField(null=True, blank=False)
    image2 = models.ImageField(null=True, blank=False)
    image3 = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url

    @property
    def imageURL1(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def imageURL2(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_signature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


from django.db import models


class StoreSalesperson(models.Model):
    salesperson_ID = models.AutoField(primary_key=True)
    salesperson_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    job_title = models.TextField()
    salary = models.IntegerField()

    # Add more fields as needed

    class Meta:
        db_table = 'store_salesperson'


class StoreTransaction(models.Model):
    transaction_id = models.CharField(max_length=200, primary_key=True, unique=True)
    total_amount = models.DecimalField(max_digits=5, decimal_places=2)
    salesperson = models.ForeignKey(StoreSalesperson, on_delete=models.CASCADE, related_name='transactions', null=True)

    # Add more fields as needed

    class Meta:
        db_table = 'store_transactions'


class region(models.Model):
    Region_ID = models.AutoField(primary_key=True)
    Region_name = models.CharField(max_length=200, null=True)
    RegionalManagerID = models.BigIntegerField(null=True)
    TotalSales = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.Region_name


class CartItem(models.Model):
    cart_id = models.BigIntegerField(null=True)

    class Meta:
        db_table = 'store_cart'


class StoreWarehouse(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=20)
    store_manager = models.TextField()  # Assuming the Store_Manager field is a text field
    salespersons = models.IntegerField()
    region_ID = models.IntegerField()

    def __str__(self):
        return f"StoreWarehouse {self.id}: {self.address}"

    class Meta:
        db_table = 'store_warehouse'
