from django import forms
from .models import Reservation
# class ReservationForm(forms.Forms):
#     name = forms.CharField(max_length=200,required=False)
#     email = forms.EmailField(max_length=50,required=False)
#    phone = forms.IntegerField(required=True)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
        # ["name","email","phone"]



