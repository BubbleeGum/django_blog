from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CategoryForm
from category.models import Category

# Create your views here.

def category_main(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category_main.html', context)

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            nama_barang = form.cleaned_data['nama_barang']
            kategori_barang = form.cleaned_data['kategori_barang']
            Category.objects.create(nama_barang=nama_barang, kategori_barang=kategori_barang)
            messages.success(request, 'Penambahan Barang berhasil')
        else:
            messages.error(request, 'Penambahan Barang gagal')
            return render(request, 'category_create.html', {'form': form})
    else:
        form = CategoryForm()
    return render(request, 'category_create.html', {'form': form})

def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success('Category Berhasil Dihapus')
    return render('category')

