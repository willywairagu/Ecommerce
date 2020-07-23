from django.shortcuts import render, redirect
from .models import BillingProfile
from django.utils.http import is_safe_url
from .forms import PaymentSelectForm
from Addresses.models import Address

#
# def payment_method_view(request):
#     form = PaymentSelectForm(request.POST or None)
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#     # print(form.errors)
#     if form.is_valid():
#         if request.method == 'POST':
#             instance = form.save(commit=False)
#             shipping_address = request.POST.get('shipping_address', None)
#             address_type = request.POST.get('address_type', 'shipping')
#             billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
#             if request.POST.get('Mpesa') == 'on':
#                 payment_type = 'Mpesa'
#                 instance.payment_type = payment_type
#                 instance.billing_profile = billing_profile
#                 instance.save()
#                 print(payment_type)
#                 request.session[payment_type + "_address_id"] = instance.id
#
#                 if shipping_address is not None:
#                     qs = Address.objects.filter(billing_profile=billing_profile, id=shipping_address)
#                     if qs.exists():
#                         request.session[address_type + "_address_id"] = shipping_address
#                     if is_safe_url(redirect_path, request.get_host()):
#                         return redirect(redirect_path)
#
#                 return render(request, 'billing/payment-method.html', {})
#             else:
#                 payment_type = "Cash"
#                 instance.payment_type = payment_type
#                 instance.billing_profile = billing_profile
#                 instance.save()
#                 print(payment_type)
#
#                 request.session[payment_type + "_address_id"] = instance.id
#                 print(payment_type + "_address_id")
#                 # shipping_address = request.POST.get('shipping_address', None)
#                 # if shipping_address is not None:
#                 #     qs = Address.objects.filter(billing_profile=billing_profile, id=shipping_address)
#                 #     if qs.exists():
#                 #         request.session[address_type + "_address_id"] = shipping_address
#                 # if is_safe_url(redirect_path, request.get_host()):
#                 #     return redirect(redirect_path)
#     else:
#         print("Error")
#
#     return redirect('cart:checkout')
#
