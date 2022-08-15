from django.db import models
from django.utils.translation import gettext as _
class Food(models.Model):
    FOOD_TYPE = [
        ("breakfast", "صبحانه"),
        ("drinks", "نهار"),
        ("lunch", "نهار"),
        ("dinner", "شام"),
    ]
    name = models.CharField(max_length=100)
    descriptions = models.CharField(_('توضیحات'),max_length=100 )
    rate = models.IntegerField(_("امتیاز"), default=0)
    price = models.IntegerField()
    time = models.IntegerField(_("زمان لازم"))
    pup_date = models.DateField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to='Food/')
    type_food= models.CharField(_("نوع غذا"), max_length=20, choices=FOOD_TYPE, default="lunch")
    def __str__(self):
        return self.name
