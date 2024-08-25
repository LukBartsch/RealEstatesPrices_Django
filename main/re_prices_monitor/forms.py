from django import forms

class SelectForm(forms.Form):
    OPTIONS = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    city = forms.ChoiceField(choices=OPTIONS, label='Select city')
    market = forms.ChoiceField(choices=OPTIONS, label='Select market')
    data_type = forms.ChoiceField(choices=OPTIONS, label='Select data type')