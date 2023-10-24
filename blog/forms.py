from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['title', 'description', 'blog_date', 'kategori_barang', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'description': forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'blog_date': forms.DateInput(attrs={'class':'form-control form-control-user', 'type': 'date'}),
            'kategori_barang': forms.Select(attrs={'class':'form-control form-control-user'}),
            'author': forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['author'].disabled = True