# forms.py
from django import forms

class InputForm(forms.Form):
    SPECIES_CHOICES = [
        ('', 'Select'),
        ('Chicken', 'Chicken'),
        ('Duck', 'Duck'),
    ]

    SSR_TYPE_CHOICES = [
        ('', 'Select'),
        ('c', 'Compound'),
        ('p1', 'Mononucleotide'),
        ('p2', 'Dinucleotide'),
        ('p3', 'Trinucleotide'),
        ('p4', 'Tetranucleotide'),
        ('p5', 'Pentanucleotide'),
        ('p6', 'Hexanucleotide'),
    ]

    species = forms.ChoiceField(choices=SPECIES_CHOICES, required=True)
    chromosome = forms.IntegerField(min_value=1, max_value=39, required=True)
    ssrtype = forms.ChoiceField(choices=SSR_TYPE_CHOICES, required=True)
    start = forms.IntegerField(min_value=1, max_value=100000, required=False)
    end = forms.IntegerField(min_value=1, max_value=100000, required=False)

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")

        if start and end and start > end:
            raise forms.ValidationError("Start position must be less than or equal to End position.")