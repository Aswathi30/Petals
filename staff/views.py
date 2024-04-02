from django.shortcuts import redirect,render
from . models import *
# Create your views here.
def staff_home(request):
    return render (request,'staff/staff_home.html')


def staff_dashboard(request):
    if 'staff' in request.session:
        return render(request,'staff/staff_dashboard.html')
    else:
        return render (request,'staff/staff_home.html')

   
    
def staff_login(request):
    if request.method=='POST':
        Email=request.POST['email']
        Password=request.POST['password']
        try:
            seller=StaffRegistration.objects.get(email=Email,password=Password)
            request.session['staff']=seller.id
            return redirect('staff:staff_dashboard')
        except StaffRegistration.DoesNotExist:
            return render(request,'staff/staff_login.html',{'msg':'InvalidEmail or Password'})
    return render(request,'staff/staff_login.html')

def addproduct_plants(request):
    categories_plants=Plants.objects.all()
    if request.method=='POST':
       name=request.POST.get('plantsname')
       description=request.POST.get('description')
       price=request.POST.get('price')
       image=request.FILES['image']
       category_plants=request.POST.get('categories_plants')
       catplants=Plants.objects.get(id=category_plants)
       product_plants=Plants_Products(name=name,description=description,price=price,image=image,category=catplants)
       product_plants.save()
    return render (request,'staff/addproduct_plants.html',{'categories_plants':categories_plants})



def view_plants(request):
    product_plants=Plants_Products.objects.all()
    return render(request,'staff/view_plants.html',{'products_plants':product_plants})

def update_plants(request,product_id):
    categories_plants=Plants.objects.all()
    product_plants=Plants_Products.objects.get(id=product_id)
    if request.method=='POST':
        name=request.POST['plantsname']
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES['image']
        category_plants=request.POST.get('categories_plants')
        catplants=Plants.objects.get(id=category_plants)

        product_plants.name=name
        product_plants.description=description
        product_plants.price=price
        product_plants.image=image
        product_plants.category=catplants
        product_plants.save()
        return redirect('staff:view_plants')

    return render(request,'staff/update_plants.html',{'categories_plants':categories_plants,'product_plants':product_plants})

def delete_plants(request,product_id):
    Plants_Products.objects.get(id=product_id).delete()
    return redirect('staff:view_plants')


def addproduct_pots(request):
    categories_pots=Pots.objects.all()
    if request.method=='POST':
       name=request.POST.get('potsname')
       description=request.POST.get('description')
       price=request.POST.get('price')
       image=request.FILES['image']
       category_pots=request.POST.get('categories_pots')
       catpots=Pots.objects.get(id=category_pots)
       product_pots=Pots_Products(name=name,description=description,price=price,image=image,category=catpots)
       product_pots.save()
    return render (request,'staff/addproduct_pots.html',{'categories_pots':categories_pots})

def view_pots(request):
    pots=Pots_Products.objects.all()
    return render(request,'staff/view_pots.html',{'pots':pots})

def update_pots(request,product_id):
    categories_pots=Pots.objects.all()
    product_pots=Pots_Products.objects.get(id=product_id)
    if request.method=='POST':
        name=request.POST['potsname']
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES['image']
        category_pots=request.POST.get('categories_pots')
        catpots=Pots.objects.get(id=category_pots)

        product_pots.name=name
        product_pots.description=description
        product_pots.price=price
        product_pots.image=image
        product_pots.category=catpots
        product_pots.save()
        return redirect('staff:view_pots')

    return render(request,'staff/update_pots.html',{'categories_pots':categories_pots,'product_pots':product_pots})


def delete_pots(request,product_id):
    Pots_Products.objects.get(id=product_id).delete()
    return redirect('staff:view_pots')


def add_pebbles(request):
    categories_pebbles=Pebbles.objects.all()
    if request.method=='POST':
       name=request.POST.get('pebblesname')
       description=request.POST.get('description')
       price=request.POST.get('price')
       image=request.FILES['image']
       category_pebbles=request.POST.get('categories_pebbles')
       catpebbles=Pebbles.objects.get(id=category_pebbles)
       product_pebbles=Pebbles_Products(name=name,description=description,price=price,image=image,category=catpebbles)
       product_pebbles.save()
    return render (request,'staff/add_pebbles.html',{'categories_pebbles':categories_pebbles})
    

def view_pebbles(request):
    pebbles=Pebbles_Products.objects.all()
    return render(request,'staff/view_pebbles.html',{'pebbles':pebbles})

def update_pebbles(request,product_id):
    categories_pebbles=Pebbles.objects.all()
    product_pebbles=Pebbles_Products.objects.get(id=product_id)
    if request.method=='POST':
        name=request.POST['pebblesname']
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES['image']
        category_pebbles=request.POST.get('categories_pebbles')
        catpebbles=Pebbles.objects.get(id=category_pebbles)

        product_pebbles.name=name
        product_pebbles.description=description
        product_pebbles.price=price
        product_pebbles.image=image
        product_pebbles.category=catpebbles
        product_pebbles.save()
        return redirect('staff:view_pebbles')

    return render(request,'staff/update_pebbles.html',{'categories_pebbles':categories_pebbles,'product_pebbles':product_pebbles})

def delete_pebbles(request,product_id):
    Pebbles_Products.objects.get(id=product_id).delete()
    return redirect('staff:view_pebbles')

def add_fertilisers(request):
    categories_fertilisers=Fertilisers.objects.all()
    if request.method=='POST':
       name=request.POST.get('fertilisersname')
       description=request.POST.get('description')
       price=request.POST.get('price')
       image=request.FILES['image']
       category_fertilisers=request.POST.get('categories_fertilisers')
       catfertilisers=Fertilisers.objects.get(id=category_fertilisers)
       product_fertilisers=Fertilisers_Products(name=name,description=description,price=price,image=image,category=catfertilisers)
       product_fertilisers.save()
    return render (request,'staff/add_fertilisers.html',{'categories_fertilisers':categories_fertilisers})

def view_fertilisers(request):
    fertilisers=Fertilisers_Products.objects.all()
    return render(request,'staff/view_fertilisers.html',{'fertilisers':fertilisers})


def update_fertilisers(request,product_id):
    categories_fertilisers=Fertilisers.objects.all()
    product_fertilisers=Fertilisers_Products.objects.get(id=product_id)
    if request.method=='POST':
        name=request.POST['fertilisersname']
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES['image']
        category_fertilisers=request.POST.get('categories_fertilisers')
        catfertilisers=Fertilisers.objects.get(id=category_fertilisers)

        product_fertilisers.name=name
        product_fertilisers.description=description
        product_fertilisers.price=price
        product_fertilisers.image=image
        product_fertilisers.category=catfertilisers
        product_fertilisers.save()
        return redirect('staff:view_fertilisers')

    return render(request,'staff/update_fertilisers.html',{'categories_fertilisers':categories_fertilisers,'product_fertilisers':product_fertilisers})


def delete_fertilisers(request,product_id):
    Fertilisers_Products.objects.get(id=product_id).delete()
    return redirect('staff:view_fertilisers')


def add_seeds(request):
    categories_seeds=Seeds.objects.all()
    if request.method=='POST':
       name=request.POST.get('seedsname')
       description=request.POST.get('description')
       price=request.POST.get('price')
       image=request.FILES['image']
       category_seeds=request.POST.get('categories_seeds')
       catseeds=Seeds.objects.get(id=category_seeds)
       product_seeds=Seeds_Products(name=name,description=description,price=price,image=image,category=catseeds)
       product_seeds.save()
    return render (request,'staff/add_seeds.html',{'categories_seeds':categories_seeds})

def view_seeds(request):
    seeds=Seeds_Products.objects.all()
    return render(request,'staff/view_seeds.html',{'seeds':seeds})

def update_seeds(request,product_id):
    categories_seeds=Seeds.objects.all()
    product_seeds=Seeds_Products.objects.get(id=product_id)
    if request.method=='POST':
        name=request.POST['seedsname']
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES['image']
        category_seeds=request.POST.get('categories_seeds')
        catseeds=Seeds.objects.get(id=category_seeds)

        product_seeds.name=name
        product_seeds.description=description
        product_seeds.price=price
        product_seeds.image=image
        product_seeds.category=catseeds
        product_seeds.save()
        return redirect('staff:view_seeds')

    return render(request,'staff/update_seeds.html',{'categories_seeds':categories_seeds,'product_seeds':product_seeds})

def delete_seeds(request,product_id):
    Seeds_Products.objects.get(id=product_id).delete()
    return redirect('staff:view_seeds')

def staff_logout(request):
    if 'staff' in request.session:
        del request.session['staff']
        return render(request,'staff/staff_home.html')
    else:
        return render(request,'customer/home.html')


