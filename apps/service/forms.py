from datetime import date

from django import forms


class RangeTimeForm(forms.Form):
    initial_date = forms.DateField(
        label="Fecha inicial",
        widget=forms.DateInput(
            attrs={
                "placeholder": "Fecha inicial",
                "type": "date",
                "max": date.today(),
            },
        ),
    )
    final_date = forms.DateField(
        label="Fecha final",
        widget=forms.DateInput(
            attrs={
                "placeholder": "Fecha final",
                "type": "date",
                "max": date.today(),
            },
        ),
    )
