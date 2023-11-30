from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
import razorpay
from django.conf import settings
from django.db.models import Sum, Avg, Count
from .models import StoreSalesperson
from .forms import OrderItemForm
from .forms import CustomerForm
from .forms import ProductForm
from django.db import IntegrityError
from .forms import StoreWarehouseForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def product(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    # Get the sorting parameter from the request
    sort_order = request.GET.get('sort', 'asc')  # Default to ascending order if not provided

    # Fetch products based on the sorting order
    if sort_order == 'asc':
        products = Product.objects.all().order_by('price')
    elif sort_order == 'desc':
        products = Product.objects.all().order_by('-price')
    else:
        # Handle invalid sorting parameter (optional)
        products = Product.objects.all()

    context = {'products': products, 'cartItems': cartItems, 'sort_order': sort_order}
    return render(request, 'store/Products.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    payment = client.order.create({'amount': order.get_cart_total * 100, 'currency': 'INR', 'payment_capture': 1})
    order.razor_pay_order_id = payment['id']
    order.save()

    context = {'items': items, 'order': order, 'payment': payment}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'CartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def sp(request):
    sproducts = Sproduct.objects.all()
    context = {'sproducts': sproducts}
    return render(request, 'store/sproduct.html', context)


def sp1(request):
    context = {}
    return render(request, 'store/sproduct1.html', context)


def sp2(request):
    context = {}
    return render(request, 'store/sproduct2.html', context)


def sp3(request):
    context = {}
    return render(request, 'store/sproduct3.html', context)


def sp4(request):
    context = {}
    return render(request, 'store/sproduct4.html', context)


def sp5(request):
    context = {}
    return render(request, 'store/sproduct5.html', context)


def sp6(request):
    context = {}
    return render(request, 'store/sproduct6.html', context)


def sp7(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.filter(BagType="HandBag")
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/sproduct7.html', context)


def sp8(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.filter(BagType="SlingBag")
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/sproduct8.html', context)


def sp9(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.filter(BagType="Wallet")
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/sproduct9.html', context)


def sp10(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.filter(BagType="Backpack")
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/sproduct10.html', context)


def sp11(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.filter(BrandName="ALDO")
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/sproduct11.html', context)


def sp12(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.filter(BrandName="Calvin Klein")
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/sproduct12.html', context)


def sp13(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.filter(BrandName="Michael Kors")
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/sproduct13.html', context)


def sp14(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.filter(BrandName="Kate Spade")
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/sproduct14.html', context)


def search_products(request):
    if request.method == 'GET':
        # Get the parameters from the query string
        name = request.GET.get('name', '')
        brand_name = request.GET.get('brand_name', '')
        bag_type = request.GET.get('bag_type', '')
        # Add more parameters as needed

        # Filter products based on the provided parameters
        products = Product.objects.filter(
            name__icontains=name,
            BrandName__icontains=brand_name,
            BagType__icontains=bag_type,
            # Add more filters based on other attributes
        )

        context = {
            'products': products,
            'name': name,
            'brand_name': brand_name,
            'bag_type': bag_type,
            # Add more context variables as needed
        }

        return render(request, 'store/Products.html', context)

    return render(request, 'store/Products.html')


def dashboard(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.all().aggregate(total_inventory=Sum('InventoryQuantity'))
    customers = Customer.objects.all().aggregate(total_users=Count('name'))
    total_revenue = StoreTransaction.objects.all().aggregate(total_price=Sum('total_amount'))
    salespersons = StoreSalesperson.objects.all().aggregate(name=Count('salesperson_name'))
    totalSales = region.objects.values('Region_name', 'TotalSales').order_by('-TotalSales')
    top_products = Product.objects.values('BagType').annotate(AverageRating=Avg('AverageRating')).order_by(
        '-AverageRating')[:4]
    context = {'products': products, 'cartItems': cartItems, 'customers': customers, 'total_revenue': total_revenue,
               'salespersons': salespersons, 'top_products': top_products, 'totalSales': totalSales}
    return render(request, 'store/dashboard.html', context)


def order_item_list(request):
    order_items = OrderItem.objects.all()
    return render(request, 'store/order_item_list.html', {'order_items': order_items})


def order_item_detail(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    return render(request, 'store/order_item_detail.html', {'order_item': order_item})


def order_item_update(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)

    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=order_item)
        if form.is_valid():
            form.save()
            return redirect('order_item_list')
    else:
        form = OrderItemForm(instance=order_item)

    return render(request, 'store/order_item_update.html', {'form': form})


def order_item_delete(request, order_item_id):
    # Get the OrderItem instance
    order_item = get_object_or_404(OrderItem, id=order_item_id)

    if request.method == 'POST':
        # Delete the OrderItem
        order_item.delete()
        # Redirect to the order items list or any other desired page
        return redirect('order_item_list')

    # Render a confirmation page before deletion
    context = {
        'order_item': order_item,
    }
    return render(request, 'store/order_item_delete.html', context)


def main(request):
    context = {}
    return render(request, 'store/index.html', context)


@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("Action:", action)
    print("Products:", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
        product.InventoryQuantity = (product.InventoryQuantity - 1)
        product.save()
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)
        product.InventoryQuantity = (product.InventoryQuantity + 1)
        product.save()
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse("Item was added", safe=False)


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'store/customer_list.html', {'customers': customers})


def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'store/customer_detail.html', {'customer': customer})


def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'store/customer_form.html', {'form': form})


def customer_update(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'store/customer_form.html', {'form': form})


def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        try:
            customer.delete()
            return redirect('customer_list')
        except IntegrityError:
            # Handle IntegrityError
            return render(request, 'store/customer_confirm_delete.html',
                          {'customer': customer, 'deletion_failed': True})

    return render(request, 'store/customer_confirm_delete.html', {'customer': customer, 'deletion_failed': False})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'store/product_form.html', {'form': form, 'action': 'Create'})


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'store/product_form.html', {'form': form, 'action': 'Update'})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'store/product_confirm_delete.html', {'product': product})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


def warehouse_list(request):
    warehouses = StoreWarehouse.objects.all()
    return render(request, 'store/warehouse_list.html', {'warehouses': warehouses})


def warehouse_detail(request, warehouse_id):
    warehouse = get_object_or_404(StoreWarehouse, id=warehouse_id)
    return render(request, 'store/warehouse_detail.html', {'warehouse': warehouse})


def warehouse_create(request):
    if request.method == 'POST':
        form = StoreWarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse_list')
    else:
        form = StoreWarehouseForm()

    return render(request, 'store/warehouse_form.html', {'form': form})


def warehouse_update(request, warehouse_id):
    warehouse = get_object_or_404(StoreWarehouse, id=warehouse_id)

    if request.method == 'POST':
        form = StoreWarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return redirect('warehouse_list')
    else:
        form = StoreWarehouseForm(instance=warehouse)

    return render(request, 'store/warehouse_form.html', {'form': form})


def warehouse_delete(request, warehouse_id):
    warehouse = get_object_or_404(StoreWarehouse, id=warehouse_id)

    if request.method == 'POST':
        try:
            warehouse.delete()
            return redirect('warehouse_list')
        except IntegrityError:
            # Handle IntegrityError
            return render(request, 'store/warehouse_confirm_delete.html',
                          {'warehouse': warehouse, 'deletion_failed': True})

    return render(request, 'store/warehouse_confirm_delete.html', {'warehouse': warehouse, 'deletion_failed': False})


def SignupPage(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Validate email format
        try:
            validate_email(email)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)

        # Validate password complexity
        try:
            validate_password(pass1)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)

        if pass1 != pass2:
            return JsonResponse({'error': "Your password and confirm password are not the same!"}, status=400)
        else:
            try:
                if User.objects.filter(username=uname).exists():
                    return JsonResponse({'error': "Username already exists. Please choose a different username."},
                                        status=400)

                # Attempt to create a user
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect('login')

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)  # Handle other exceptions
    else:
        # Handle GET requests or render signup form
        # ...

        return render(request, 'store/signup.html', context)


def LoginPage(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')  # Changed variable name for password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context['error'] = "Username or Password is incorrect!!!"
            return render(request, 'store/login.html', context)

    return render(request, 'store/login.html', context)


def EmployeeSignupPage(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Validate email format
        try:
            validate_email(email)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)

        # Validate password complexity
        try:
            validate_password(pass1)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)

        if pass1 != pass2:
            return JsonResponse({'error': "Your password and confirm password are not the same!"}, status=400)
        else:
            try:
                if User.objects.filter(username=uname).exists():
                    return JsonResponse({'error': "Username already exists. Please choose a different username."},
                                        status=400)

                # Attempt to create a user
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect('EmployeeLoginPage')

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)  # Handle other exceptions
    else:
        # Handle GET requests or render signup form
        return render(request, 'store/EmployeeSignup.html', context)


def EmployeeLoginPage(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')  # Changed variable name for password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context['error'] = "Username or Password is incorrect!!!"
            return render(request, 'store/EmployeeLogin.html', context)

    return render(request, 'store/EmployeeLogin.html', context)



