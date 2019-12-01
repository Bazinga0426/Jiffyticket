from django import forms
from .models import Order


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
<<<<<<< HEAD
        fields = ('cinema', 'session', 'adult_counts', 'student_counts', 'child_counts')
=======
        fields = ('adult_counts', 'student_counts', 'child_counts',  'session')
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705

    def save(self, commit=True):
        m = super(OrderModelForm, self).save(commit=False)
        # do custom stuff
        if commit:
            m.save()
        return m
