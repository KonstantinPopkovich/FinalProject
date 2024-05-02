from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet,
    AuthorsViewSet,
    BooksViewSet,
    ManufacturerViewSet,
    ModelViewSet,
    EBooksViewSet,
    EBooks_other_shopsViewSet,
    OfficeSuppliesViewSet,
    PenViewSet,
    PencilViewSet,
    PaperViewSet,
    NotebookViewSet,
    ClipViewSet,
    EnvelopeViewSet,
    PaintViewSet,
    MarkerViewSet
)

router = routers.DefaultRouter()


router.register('categories', CategoryViewSet)
router.register('authors', AuthorsViewSet)
router.register('books', BooksViewSet)
router.register('manufacturers', ManufacturerViewSet)
router.register('models', ModelViewSet)
router.register('ebooks', EBooksViewSet)
router.register('ebooks-other-shops', EBooks_other_shopsViewSet)
router.register('office-supplies', OfficeSuppliesViewSet)
router.register('pens', PenViewSet)
router.register('pencils', PencilViewSet)
router.register('papers', PaperViewSet)
router.register('notebooks', NotebookViewSet)
router.register('clips', ClipViewSet)
router.register('envelopes', EnvelopeViewSet)
router.register('paints', PaintViewSet)
router.register('markers', MarkerViewSet)

urlpatterns = router.urls