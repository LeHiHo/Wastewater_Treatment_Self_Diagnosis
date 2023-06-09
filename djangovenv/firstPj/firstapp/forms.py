from django import forms
class DataForm(forms.Form):
    title = forms.CharField(max_length = 10)
    content = forms.CharField(widget = forms.Textarea)
