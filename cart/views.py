from django.shortcuts import render,redirect
from staff.models import *
from customer.models import *
from.models import *
from django.http import HttpResponse
# Create your views here.

def cart(request):
    
    if 'customer' in request.session:
        cart_items = Cart.objects.all()
        grand_total = 0
    
        for item in cart_items:
            if item.plants:
                grand_total += item.plants.price * item.plants_quantity
            if item.pots:
                grand_total += item.pots.price * item.pots_quantity
            try:
                if item.pebbles:
                
                    grand_total += item.pebbles.price * item.pebbles_quantity
            except Pebbles_Products.DoesNotExist:
                    # Handle the case where Pebbles_Products object does not exist
                    # You can choose to skip this item or handle it differently
                    pass
                
                
            if item.fertilisers:
                grand_total += item.fertilisers.price * item.fertilisers_quantity
            if item.seeds:
                grand_total += item.seeds.price * item.seeds_quantity
       
        return render(request, 'customer/cart.html', {'cart_items': cart_items, 'grand_total': grand_total})
    else:
        return render(request,'customer/home.html')

def add_to_cart(request,product_id):
    if 'customer' in request.session:
        if request.method=='POST':
        
            
            product=Plants_Products.objects.get(id=product_id)
            cart_item,created=Cart.objects.get_or_create(plants=product)
            if not created:
                    cart_item.plants_quantity+=1
                    cart_item.save()
                
            return redirect('cart:cart')
        else:
            return render(request,'customer/home.html')

def add_to_cart_pot(request,product_id):
    if 'customer' in request.session:
        if request.method=='POST':
        
            
            product=Pots_Products.objects.get(id=product_id)
            cart_item,created=Cart.objects.get_or_create(pots=product)
            if not created:
                    cart_item.pots_quantity+=1
                    cart_item.save()
                
        return redirect('cart:cart')
    else:   
        return render(request,'customer/home.html')

def add_to_cart_seeds(request,product_id):
    if 'customer' in request.session:
        if request.method=='POST':
        
            
            product=Seeds_Products.objects.get(id=product_id)
            cart_item,created=Cart.objects.get_or_create(seeds=product)
            if not created:
                    cart_item.seeds_quantity+=1
                    cart_item.save()
    
        return redirect('cart:cart')   
    else: 
        return render(request,'customer/home.html')

def add_to_cart_fertilisers(request,product_id):
    if 'customer' in request.session:
        if request.method=='POST':
        
            
            product=Fertilisers_Products.objects.get(id=product_id)
            cart_item,created=Cart.objects.get_or_create(fertilisers=product)
            if not created:
                    cart_item.fertilisers_quantity+=1
                    cart_item.save()
            return redirect('cart:cart') 
    else:

        return render(request,'customer/home.html')

def add_to_cart_pebbles(request,product_id):
    if 'customer' in request.session:
        if request.method=='POST':
        
            product=Pebbles_Products.objects.get(id=product_id)
            cart_item,created=Cart.objects.get_or_create(pebbles=product)
            if not created:
                    cart_item.pebbles_quantity+=1
                    cart_item.save()
        return redirect('cart:cart')
    else: 
        return render(request,'customer/home.html')

def remove_from_cart(request,product_id):
    if request.method=='POST':
     
        product=Plants_Products.objects.get(id=product_id)
        cart_item=Cart.objects.get(plants=product)

        cart_item.delete()
  
        return redirect('cart:cart')
    else: 
        return render(request,'customer/home.html')

def remove_from_cart_pots(request,product_id):
    if request.method=='POST':
     
        product=Pots_Products.objects.get(id=product_id)
        cart_item=Cart.objects.get(pots=product)

        cart_item.delete()
  
    return redirect('cart:cart')
   
def remove_from_cart_seeds(request,product_id):
    if request.method=='POST':
     
        product=Seeds_Products.objects.get(id=product_id)
        cart_item=Cart.objects.get(seeds=product)

        cart_item.delete()
  
    return redirect('cart:cart')

def remove_from_cart_pebbles(request,product_id):
    if request.method=='POST':
     
        product=Pebbles_Products.objects.get(id=product_id)
        cart_item=Cart.objects.get(pebbles=product)

        cart_item.delete()
  
    return redirect('cart:cart')

def remove_from_cart_fertilisers(request,product_id):
    if request.method=='POST':
     
        product=Fertilisers_Products.objects.get(id=product_id)
        cart_item=Cart.objects.get(fertilisers=product)

        cart_item.delete()
  
    return redirect('cart:cart')
