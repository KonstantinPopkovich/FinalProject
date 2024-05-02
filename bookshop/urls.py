from django.urls import path
from . import views
from .views import (IndexView,
                    BookDetailView,
                    EBookDetailView,
                    EBooksOtherShopsView,
                    OfficeSuppliesDetailView,
                    Pen,
                    Pencil,
                    Paper,
                    Notebook,
                    Clip,
                    Envelope,
                    Paint,
                    Marker
                    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('ebooks/<int:pk>/', EBookDetailView.as_view(), name='ebook_detail'),
    path('ebooks/other_shops/', EBooksOtherShopsView.as_view(), name='ebooks_other_shops'),
    path('office-supplies/<int:pk>/', views.OfficeSuppliesDetailView.as_view(), name='office_supplies_detail'),
    path('pen/<int:pk>/', views.pen_detail, name='pen_detail'),
    path('pencil/<int:pk>/', views.pencil_detail, name='pencil_detail'),
    path('paper/<int:pk>/', views.paper_detail, name='paper_detail'),
    path('notebook/<int:pk>/', views.notebook_detail, name='notebook_detail'),
    path('clip/<int:pk>/', views.clip_detail, name='clip_detail'),
    path('envelope/<int:pk>/', views.envelope_detail, name='envelope_detail'),
    path('paint/<int:pk>/', views.paint_detail, name='paint_detail'),
    path('marker/<int:pk>/', views.marker_detail, name='marker_detail'),
]
