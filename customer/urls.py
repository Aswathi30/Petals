from django.urls import path
from . import views 
app_name='customer'
urlpatterns=[
   
    
    path('',views.home,name='home'),
    path('customer_dashboard/<str:category>',views.customer_dashboard,name='customer_dashboard'),
    path('search/',views.search,name='search'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('paynow/',views.paynow,name='paynow')
]