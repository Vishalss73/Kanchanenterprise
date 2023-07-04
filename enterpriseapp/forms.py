from django import forms 
from django.forms import inlineformset_factory
from .models import PhoneNumber, EmailAddress, Contact_details
class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number']

class EmailAddressForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ['email_address']
ContactFormSet = inlineformset_factory(Contact_details,PhoneNumber, form=PhoneNumberForm, extra = 1, can_delete=True )
EmailFormSet = inlineformset_factory(Contact_details,EmailAddress, form=EmailAddressForm, extra = 1, can_delete=True)        

class Contact_detailsForm(forms.ModelForm):
    class Meta:
        model = Contact_details
        fields = '__all__'

    phone_numbers = inlineformset_factory(Contact_details,PhoneNumber, form=PhoneNumberForm, extra = 1, can_delete=True )
    email_addresss = inlineformset_factory(Contact_details,EmailAddress, form=EmailAddressForm, extra = 1, can_delete=True)            