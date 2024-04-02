from django.urls import path
from .import views
app_name='staff'
urlpatterns= [
    path('',views.staff_home,name='staff_home'),
    path('staff_login/',views.staff_login,name='staff_login'),
    path('staff_dashboard/',views.staff_dashboard,name='staff_dashboard'),
    path('staff_logout/',views.staff_logout,name='staff_logout'),

    path('addproduct_plants/',views.addproduct_plants,name='add_plants'),
    path('view_plants/',views.view_plants,name='view_plants'),
    path('update_plants/<int:product_id>',views.update_plants,name='update_plants'),
    path('delete_plants/<int:product_id>',views.delete_plants,name='delete_plants'),

    path('addproduct_pots/',views.addproduct_pots,name='addproduct_pots'),
    path('view_pots/',views.view_pots,name='view_pots'),
    path('update_pots/<int:product_id>',views.update_pots,name='update_pots'),
    path('delete_pots/<int:product_id>',views.delete_pots,name='delete_pots'),


    path('add_pebbles/',views.add_pebbles,name='add_pebbles'),
    path('view_pebbles/',views.view_pebbles,name='view_pebbles'),
    path('update_pebbles/<int:product_id>',views.update_pebbles,name='update_pebbles'),
    path('delete_pebbles/<int:product_id>',views.delete_pebbles,name='delete_pebbles'),

    path('add_fertilisers/',views.add_fertilisers,name='add_fertilisers'),
    path('view_fertilisers/',views.view_fertilisers,name='view_fertilisers'),
    path('update_fertilisers/<int:product_id>',views.update_fertilisers,name='update_fertilisers'),
    path('delete_fertilisers/<int:product_id>',views.delete_fertilisers,name='delete_fertilisers'),

    path('add_seeds/',views.add_seeds,name='add_seeds'),
    path('view_seeds/',views.view_seeds,name='view_seeds'),
    path('update_seeds/<int:product_id>',views.update_seeds,name='update_seeds'),
    path('delete_seeds/<int:product_id>',views.delete_seeds,name='delete_seeds'),



]