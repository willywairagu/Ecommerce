from django.db import models
from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping')
)
PAYMENT_TYPES = (
    ('mpesa', 'Mpesa'),
    ('cash', 'Cash')
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    payment_type = models.CharField(max_length=120, choices=PAYMENT_TYPES, default='Mpesa')
    city = models.CharField(max_length=120, default="KAJIADO")
    Area = models.CharField(max_length=120)
    Phone_number = models.IntegerField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{line1}\n{city}\n{Area}".format(
            line1=self.Phone_number,
            city=self.city,
            Area =self.Area
        )
