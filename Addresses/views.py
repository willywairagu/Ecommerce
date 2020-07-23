from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from .forms import AddressForm
from billing.models import BillingProfile
from billing.forms import PaymentSelectForm
from billing.LipaNaMpesa import lipa_na_mpesa
from .models import Address
from orders.models import Order


def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    form2 = PaymentSelectForm(request.POST or None)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        print(request.POST)
        instance = form.save(commit=False)
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

        if billing_profile is not None:
            address_type = request.POST.get('address_type', 'shipping')
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()
            request.session[address_type + "_address_id"] = instance.id
            print(address_type + "_address_id")

            # if request.POST.get('Mpesa') == 'on':
            #     choice = 'Mpesa'
            #     Order.update_payment_type(request.POST, choice=choice)
            #     BillingProfile.Mpesa_number = request.POST.get("Mpesa_number")
            #     print("_______________________")
            #     lipa_na_mpesa(BillingProfile.Mpesa_number)

                # return render(request, 'billing/payment-method.html', {})
            #
            # if request.POST.get('COD') == 'on':
            #     choice = 'Cash'
            #     Order.update_payment_type(request, choice=choice)
        else:
            print("error here")
            return redirect("cart:checkout")
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        #
        # if request.POST.get('Mpesa') == 'on':
        #     payment_type = 'Mpesa'
        #     instance.payment_type = payment_type
        #     print(payment_type)
        # if request.POST.get('COD') == 'on':
        #     payment_type = 'Cash'
        #     instance.payment_type = payment_type
        #     print(payment_type)

    return redirect('cart:checkout')


def checkout_address_reuse_view(request):
    if request.user.is_authenticated:
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        if request.method == 'POST':
            print(request.POST)
            shipping_address = request.POST.get('shipping_address', None)
            address_type = request.POST.get('address_type', 'shipping')
            billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
            if shipping_address is not None:
                qs = Address.objects.filter(billing_profile=billing_profile, id=shipping_address)
                if qs.exists():
                    request.session[address_type + "_address_id"] = shipping_address
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
            # if request.POST.get('Mpesa') == 'on':
            #     payment_type = 'Mpesa'
            #     print(payment_type)
            # if request.POST.get('COD') == 'on':
            #     payment_type = 'Cash'
            #     print(payment_type)

    return redirect('cart:checkout')
