from django import forms
from .models import Function


class NewFunctionForm(forms.Form):
    formula = forms.CharField(max_length=64)
    dt = forms.IntegerField()
    interval = forms.IntegerField()

    def clean_formula(self):
        formula = self.cleaned_data['formula']
        if formula == '':
            raise forms.ValidationError('Empty field', code=0)
        return formula

    def clean_dt(self):
        dt = self.cleaned_data['dt']
        if dt == '':
            raise forms.ValidationError('Empty field', code=0)
        return dt

    def clean_interval(self):
        interval = self.cleaned_data['interval']
        if interval == '':
            raise forms.ValidationError('Empty field', code=0)
        return interval

    def save(self):
        function = Function(**self.cleaned_data)
        function.owner = self._user
        function.save()
        return function
