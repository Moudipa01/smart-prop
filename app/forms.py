from django import forms

class TransferForm(forms.Form):
    receiver_address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}),
                             label="Address of the buyer")
    amount = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}),
                             label="Amount of Ethereum to be Paid")
    message = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}),
                             label="Message to be sent")