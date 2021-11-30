from django import forms
from string import Template
from django.utils.safestring import mark_safe
from .models import Articles
from django.forms import ModelForm, fields, TextInput, widgets, Textarea, ImageField

# class PictureWidget(forms.widgets.Widget):
#     def render(self,attrs={
#                 'class':'form-control',
#                 'placeholder':'Product image'
#     }, **kwargs):
#         html =  Template("""<img src="$link"/>""")
#         return mark_safe(html.substitute(link=value))

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'price']

        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Product name'
            }),
            #'prod_image':ImageField(widget=PictureWidget),
            'price':Textarea(attrs={
                'class':'form-control',
                'placeholder':'Product description'
            }),
        }