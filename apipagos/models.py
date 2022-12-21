from django.db import models
from users.models import User

from datetime import timedelta, date
expiration = date.today() + timedelta(days=1)

class Service(models.Model):
    name =  models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    logo = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class PaymentUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users1')
    servide = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='services1')
    amount = models.FloatField(default=0.0)
    payment_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(default=expiration)

    def __str__(self):
        return str(self.user)
        

class ExproredPaument(models.Model):
    payment_user = models.ForeignKey(PaymentUser, on_delete=models.CASCADE,related_name='pagouser')
    penalty_fee_amount = models.FloatField(default=5.0)

    def __str__(self):
        return self.payment_user


