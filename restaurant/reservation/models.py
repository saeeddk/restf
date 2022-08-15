from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Reservation(models.Model):
    name = models.CharField(_("نام و نام خاوادگی"),max_length=200)
    email = models.CharField(_("آدرس الکترونیکی"), max_length=50)
    phone = models.CharField(_("تلفن"), max_length=20)
    number = models.IntegerField(_("تعداد"))
    date = models.DateField(_("تاریخ"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("ساعت"), auto_now=False, auto_now_add=False)

def __str__(self):
    return self.name
