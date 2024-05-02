from rest_framework import mixins, viewsets, generics
from bookshop.models import *
from .serializers import *
from .permissions import IsAdminOrReadOnly

class Mixins(mixins.ListModelMixin,
             mixins.RetrieveModelMixin,
             mixins.CreateModelMixin,
             mixins.UpdateModelMixin,
             mixins.DestroyModelMixin,
             viewsets.GenericViewSet
             ):
    pass

class CategoryViewSet(Mixins):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class AuthorsViewSet(Mixins):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [IsAdminOrReadOnly]
class BooksViewSet(Mixins):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAdminOrReadOnly]

class ManufacturerViewSet(Mixins):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAdminOrReadOnly]

class ModelViewSet(Mixins):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAdminOrReadOnly]

class EBooksViewSet(Mixins):
    queryset = EBooks.objects.all()
    serializer_class = EBooksSerializer
    permission_classes = [IsAdminOrReadOnly]

class EBooks_other_shopsViewSet(Mixins):
    queryset = EBooks_other_shops.objects.all()
    serializer_class = EBooks_other_shopsSerializer
    permission_classes = [IsAdminOrReadOnly]

class OfficeSuppliesViewSet(Mixins):
    queryset = OfficeSupplies.objects.all()
    serializer_class = OfficeSuppliesSerializer
    permission_classes = [IsAdminOrReadOnly]

class PenViewSet(Mixins):
    queryset = Pen.objects.all()
    serializer_class = PenSerializer
    permission_classes = [IsAdminOrReadOnly]

class PencilViewSet(Mixins):
    queryset = Pencil.objects.all()
    serializer_class = PencilSerializer
    permission_classes = [IsAdminOrReadOnly]

class PaperViewSet(Mixins):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    permission_classes = [IsAdminOrReadOnly]

class NotebookViewSet(Mixins):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    permission_classes = [IsAdminOrReadOnly]

class ClipViewSet(Mixins):
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer
    permission_classes = [IsAdminOrReadOnly]

class EnvelopeViewSet(Mixins):
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer
    permission_classes = [IsAdminOrReadOnly]

class PaintViewSet(Mixins):
    queryset = Paint.objects.all()
    serializer_class = PaintSerializer
    permission_classes = [IsAdminOrReadOnly]

class MarkerViewSet(Mixins):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    permission_classes = [IsAdminOrReadOnly]