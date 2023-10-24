from django import forms

class CategoryForm(forms.Form):
    nama_barang = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder':'Masukkan Nama'}))
    kategori_barang = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder':'Masukkan Kategori'}))