from django import forms
from .models import Transactions
from account.models import Account, Kyc


class DepositForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            "amount",
            "method",
            "prove_img",
            "trans_type",
        ]


class KycForm(forms.ModelForm):
    class Meta:
        model = Kyc
        fields = [
            "document_front",
            "document_back",
        ]


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "profile_image",
            "last_name",
            "first_name",
            "gender",
            "country",
            "region",
            "city",
            "address",
            "zipcode",
        ]
