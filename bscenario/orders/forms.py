from django import forms
from .models import Order


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('adult_counts', 'student_counts', 'child_counts',  'session')

    def save(self, commit=True):
        m = super(OrderModelForm, self).save(commit=False)
        # do custom stuff
        if commit:
            m.save()
        return m
