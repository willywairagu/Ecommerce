
from django.urls import path

from carts.views import (
    cart_home,
    checkout_home,
    cart_update,
    checkout_done_view
)

urlpatterns = [
    path('', cart_home, name='home'),
    path('checkout/', checkout_home, name='checkout'),
    path('checkout/success/', checkout_done_view, name='success'),
    path('update/', cart_update, name='update')

]
app_name = "carts"
