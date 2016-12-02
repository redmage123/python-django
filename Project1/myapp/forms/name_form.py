from django import forms

class NameForm(forms.Form):
    ''' This is the doc string for the NameForm class '''
    your_name = forms.CharField(label = 'Your name', max_length = 30)

