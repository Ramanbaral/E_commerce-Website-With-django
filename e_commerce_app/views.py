from django.shortcuts import render,redirect,HttpResponse
from .models import product,order,customer
import datetime


def index(request):
    products=product.objects.all()
    return render(request,'e_commerce_app/index.html',{'products':products})

def cart(request):
    #getting the order of loged in user only
    customer_order=customer.objects.get(user=request.user)
    orders=order.objects.filter(customer=customer_order)
    if len(orders) ==0:
        return render(request,'e_commerce_app/cart.html',{'message':'No Items in cart'})
    #to get total amount of cart and total items in cart
    total_amount_cart=0
    total_items_cart=0
    for i in orders:
        total_amount_cart+=i.product.price * i.quantity
        total_items_cart+=i.quantity
    return render(request,'e_commerce_app/cart.html',{'orders':orders,'total_amount_cart':total_amount_cart,'total_items_cart':total_items_cart})

def checkout(request):
    customer_order=customer.objects.get(user=request.user)
    orders=order.objects.filter(customer=customer_order)
    if len(orders) == 0:
        return render(request,'e_commerce_app/checkout.html',{'message':'No Items in cart'})
        
    total_amount_cart=0
    total_items_cart=0
    for i in orders:
        total_amount_cart+=i.product.price * i.quantity
        total_items_cart+=i.quantity
    return render(request,'e_commerce_app/checkout.html',{'orders':orders,'total_amount_cart':total_amount_cart,'total_items_cart':total_items_cart})

def addtocart(request,pk):
    #need to be fix does not work.
    current_date=datetime.date.today()
    user=customer.objects.get(user=request.user)
    selected_product=product.objects.filter(id=pk)[0]
    #checking wherther the order already exists or not for this user if exists the increment the quantity
    o=order.objects.filter(customer=user,product=selected_product).exists()
    if (o):
        finding_order=order.objects.filter(customer=user,product=selected_product).first()
        finding_order.quantity=finding_order.quantity + 1
        print(finding_order.quantity)
    else:
        user_order=order(customer=user,product=selected_product,date_of_order=current_date,quantity=1)
        user_order.save()
    return redirect('shop-home')

def delete_cart_item(request,pk):
    cart_item=order.objects.get(id=pk)
    cart_item.delete()
    return redirect('shop-cart')

def product_view(request,pk):
    query_product=product.objects.get(id=pk)
    products=product.objects.filter(category=query_product.category)[:6]
    return render(request,'e_commerce_app/product_view.html',{'product':query_product,'products':products})

def search(request):
    query=request.GET.get('search')
    products=product.objects.filter(name__icontains=query)
    return render(request,'e_commerce_app/search.html',{'products':products})

def category(request,category):
    products=product.objects.filter(category=category)
    return render(request,'e_commerce_app/category.html',{'category':category,'products':products})