from django import forms


class DateTime(forms.Form):
    my_date_field = forms.DateField()