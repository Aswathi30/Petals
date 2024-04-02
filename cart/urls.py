from django.urls import path
from.import views 
app_name='cart'
urlpatterns=[
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/<str:product_id>',views.add_to_cart,name='add_to_cart'),
    path('add_to_cart_pot/<str:product_id>',views.add_to_cart_pot,name='add_to_cart_pot'),
    path('add_to_cart_seeds/<str:product_id>',views.add_to_cart_seeds,name='add_to_cart_seeds'),
    path('add_to_cart_fertilisers/<str:product_id>',views.add_to_cart_fertilisers,name='add_to_cart_fertilisers'),
    path('add_to_cart_pebbles/<str:product_id>',views.add_to_cart_pebbles,name='add_to_cart_pebbles'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('remove_from_cart_pots/<int:product_id>',views.remove_from_cart_pots,name='remove_from_cart_pots'),
    path('remove_from_cart_seeds/<int:product_id>',views.remove_from_cart_seeds,name='remove_from_cart_seeds'),
    path('remove_from_cart_pebbles/<int:product_id>',views.remove_from_cart_pebbles,name='remove_from_cart_pebbles'),
    path('remove_from_cart_fertilisers/<int:product_id>',views.remove_from_cart_fertilisers,name='remove_from_cart_fertilisers'),

]
