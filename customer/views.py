from django.shortcuts import render,redirect
from.models import *
from staff.models import *
from django.http import HttpResponse
# # Create your views here.
def hello(request):
    return HttpResponse('hello')
def home(request):
    return render(request,'customer/home.html')

def customer_dashboard(request,category):
   if 'customer' in request.session: 

    try:
        if Plants.objects.filter(name=category).exists():
            p=Plants.objects.get(name=category)
            plants=Plants_Products.objects.filter(category=p)
            return render(request,'customer/customer_dashboard.html',{'plants':plants})

        elif Pots.objects.filter(name=category).exists():
            o=Pots.objects.get(name=category)
            pots=Pots_Products.objects.filter(category=o)
            return render(request,'customer/customer_dashboard.html',{'pots':pots})

        elif Pebbles.objects.filter(name=category).exists():
            b=Pebbles.objects.get(name=category)
            pebbles=Pebbles_Products.objects.filter(category=b)
            return render(request,'customer/customer_dashboard.html',{'pebbles':pebbles})

        elif Fertilisers.objects.filter(name=category).exists():
            f=Fertilisers.objects.get(name=category)
            fertilisers=Fertilisers_Products.objects.filter(category=f)
            return render(request,'customer/customer_dashboard.html',{'fertilisers':fertilisers})
    
        elif Seeds.objects.filter(name=category).exists():
            s=Seeds.objects.get(name=category)
            seeds=Seeds_Products.objects.filter(category=s)

            return render(request,'customer/customer_dashboard.html',{'seeds':seeds})
    except:
         
            plants=Plants_Products.objects.all()
            pots=Pots_Products.objects.all()
            pebbles=Pebbles_Products.objects.all()
            fertilisers=Fertilisers_Products.objects.all()
            seeds=Seeds_Products.objects.all()
            return render(request,'customer/customer_dashboard.html',{'plants':plants,'pots':pots,'pebbles':pebbles,'fertilisers':fertilisers,'seeds':seeds})
   else:
        return render(request,'customer/home.html')

def search(request):
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            plants=Plants_Products.objects.filter(description__icontains=keyword)
            pots=Pots_Products.objects.filter(description__icontains=keyword)
            pebbles=Pebbles_Products.objects.filter(description__icontains=keyword)
            fertilisers=Fertilisers_Products.objects.filter(description__icontains=keyword)
            seeds=Seeds_Products.objects.filter(description__icontains=keyword)


        context={
            'plants':plants,
             'pots':pots,
             'pebbles':pebbles,
             'fertilisers':fertilisers,
             'seeds':seeds,

        }
    return render(request,'customer/customer_dashboard.html',context)


def login(request):
    if request.method=='POST':
        Email=request.POST['email']
        Password=request.POST['password']
        try:
            cust=Customer.objects.get(email=Email,password=Password)
            request.session['customer']=cust.id
            plants=Plants_Products.objects.all()
            pots=Pots_Products.objects.all()
            pebbles=Pebbles_Products.objects.all()
            fertilisers=Fertilisers_Products.objects.all()
            seeds=Seeds_Products.objects.all()
            return render(request,'customer/customer_dashboard.html',{'plants':plants,'pots':pots,'pebbles':pebbles,'fertilisers':fertilisers,'seeds':seeds})
        except Customer.DoesNotExist:
            return render(request,'customer/login.html',{'msg':'invalid username or password'})
    return render(request,'customer/login.html')

def signup(request):
    if request.method=='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Password=request.POST['password']
        customer=Customer(name=Name,email=Email,password=Password)
        customer.save()
        return redirect('customer:login')
    return render (request,'customer/signup.html')

def logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return render(request,'customer/home.html')
    else:
      return render (request,'customer/home.html')

def paynow(request):
    return render(request,'customer/paynow.html')
