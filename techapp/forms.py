from django import forms

class PostForm(forms.Form):
    image = forms.FileField()
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Input title','class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Description','class':'form-control'}),required=True)
    