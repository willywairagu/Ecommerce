from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import home_page, about_page, contact_page

# from billing.views import
from Addresses.views import checkout_address_create_view, checkout_address_reuse_view
from accounts.views import LoginView, RegisterView, guest_register_view
from carts.views import cart_detail_api_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home_page, name="Home"),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('home/', include("products.urls", namespace="products"), name="Home"),
    path('about/', about_page, name="About"),
    path('contact/', contact_page, name="Contact"),
    path('login/', LoginView.as_view(), name="Login"),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('register/guest/', guest_register_view, name="Guest_register"),
    path('logout/', LogoutView.as_view(), name="Logout"),
    path('api/cart/', cart_detail_api_view, name="api-cart"),
    path('cart/', include("carts.urls", namespace="cart")),
    path('register/', RegisterView.as_view(), name="Register"),
    # path('billing/payment-method/', payment_method_view, name="billing-payment-method"),
    path('bootsrap/', TemplateView.as_view(template_name="bootsrap/example.html")),
    path('search/', include("search.urls", namespace="search")),
    path('products/', include("products.urls", namespace="products"))
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
