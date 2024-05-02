from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import (Books,
                     Authors,
                     Category,
                     EBooks,
                     Manufacturer,
                     Model,
                     EBooks_other_shops,
                     OfficeSupplies,
                     Pen,
                     Pencil,
                     Paper,
                     Notebook,
                     Clip,
                     Envelope,
                     Paint,
                     Marker)

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        return Books.objects.order_by('-id')[:5]

class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'book_detail.html'

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def authors_list(request):
    authors = Authors.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

class EBookDetailView(generic.DetailView):
    model = EBooks
    template_name = 'ebook_detail.html'

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'your_app/manufacturer_list.html', {'manufacturers': manufacturers})

def model_list(request):
    models = Model.objects.all()
    return render(request, 'your_app/model_list.html', {'models': models})

class EBooksOtherShopsView(generic.ListView):
    model = EBooks_other_shops
    template_name = 'ebooks_other_shops.html'


class OfficeSuppliesDetailView(generic.DetailView):
    model = OfficeSupplies
    template_name = 'office_supplies_detail.html'

def pen_detail(request, pk):
    pen = get_object_or_404(Pen, pk=pk)
    return render(request, 'pen_detail.html', {'pen': pen})

def pencil_detail(request, pk):
    pencil = get_object_or_404(Pencil, pk=pk)
    return render(request, 'pencil_detail.html', {'pencil': pencil})

def paper_detail(request, pk):
    paper = get_object_or_404(Paper, pk=pk)
    return render(request, 'paper_detail.html', {'paper': paper})

def notebook_detail(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    return render(request, 'notebook_detail.html', {'notebook': notebook})

def clip_detail(request, pk):
    clip = get_object_or_404(Clip, pk=pk)
    return render(request, 'clip_detail.html', {'clip': clip})

def envelope_detail(request, pk):
    envelope = get_object_or_404(Envelope, pk=pk)
    return render(request, 'envelope_detail.html', {'envelope': envelope})

def paint_detail(request, pk):
    paint = get_object_or_404(Paint, pk=pk)
    return render(request, 'paint_detail.html', {'paint': paint})

def marker_detail(request, pk):
    marker = get_object_or_404(Marker, pk=pk)
    return render(request, 'marker_detail.html', {'marker': marker})
