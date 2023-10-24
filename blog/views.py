from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BlogForm
from .models import Blog, Category

def blog_main(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog_main.html', context)

def blog_create(request):
    instance = Blog(author=request.user.username)
    form = BlogForm(instance=instance)
    return render(request, 'blog_create.html', {'form': form})
                

def blog_store(request):
    author = request.user.username
    title = request.POST.get('title')
    description = request.POST.get('description')
    kategori_barang = request.POST.get('kategori_barang')
    kategori_barang_instance = Category.objects.get(id=kategori_barang)
    blog_date = request.POST.get('blog_date')
    Blog.objects.create(author=author, title=title, description=description, kategori_barang=kategori_barang_instance, blog_date=blog_date)
    
    return redirect('blog') 
        
def blog_edit(request, id):
    blogs = get_object_or_404(Blog, id=id)
    context = {
        'blogs' : blogs
    }
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog berhasil diperbarui.')
            return redirect('blog_detail', blog_id=blogs)
    else:
        form = BlogForm(instance=blogs)
        
    return render(request, 'blog_edit.html', context)

# def blog_update

def blog_delete(request, id):
    blogs = get_object_or_404(Category, id=id)
    blogs.delete()
    messages.success('Category Berhasil Dihapus')
    return render('blogs')
    
        

