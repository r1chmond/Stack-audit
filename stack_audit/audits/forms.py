from django import forms

from audits.models import SmartContract


class SmartContractForm(forms.ModelForm):
    class Meta:
        model = SmartContract
        fields = ['contract']
