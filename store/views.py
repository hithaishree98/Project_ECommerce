from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
import razorpay
from django.conf import settings
from django.db.models import Sum, Avg , Count
# Create your views here.

def product(request):
      if request.user.is_authenticated:
            customer=request.user.customer
            order, created=Order.objects.get_or_create(customer=customer,complete=False)
            items=order.orderitem_set.all()
            cartItems=order.get_cart_items
      else:
            items=[]
            order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
            cartItems=order['get_cart_items']
      products=Product.objects.all()
      context = {'products':products,'cartItems':cartItems}
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
    payment = client.order.create({'amount': order.get_cart_total * 100, 'currency': 'USD', 'payment_capture': 1})
    order.razor_pay_order_id = payment['id']
    order.save()

    context = {'items': items, 'order': order, 'payment': payment}
    return render(request, 'store/cart.html', context)

def checkout(request):
      if request.user.is_authenticated:
            customer=request.user.customer
            order, created=Order.objects.get_or_create(customer=customer,complete=False)
            items=order.orderitem_set.all()
      else:
            items=[]
            order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
            cartItems=order['get_cart_items']
      context = {'items':items, 'order':order,'CartItems':cartItems}
      return render(request, 'store/checkout.html', context)

def contact(request):
	context = {}
	return render(request, 'store/contact.html', context)
def sp(request):
      sproducts=Sproduct.objects.all()
      context = {'sproducts':sproducts}
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
    top_products = Product.objects.values('BagType').annotate(AverageRating=Avg('AverageRating')).order_by('-AverageRating')[:4]
    print(products)
    print(customers)
    print(total_revenue)
    print(salespersons)
    print(totalSales)

    print(top_products)
    context = {'products': products, 'cartItems': cartItems,'customers':customers,'total_revenue':total_revenue,'salespersons':salespersons,'top_products':top_products,'totalSales':totalSales}
    return render(request, 'store/dashboard.html', context)

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
    order, created = Order.objects.get_or_create(customer=customer , complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order= order,product=product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity +1)  
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity -1)    
    orderitem.save()
    
    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse("Item was added", safe=False)


