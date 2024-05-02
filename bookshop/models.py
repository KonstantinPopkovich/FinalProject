from django.db import models

class Category(models.Model):
    name_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Authors(models.Model):
    name_authors = models.CharField(max_length=100)

    def __str__(self):
        return self.name_authors

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Books(models.Model):
    writer = models.ForeignKey(Authors, on_delete=models.CASCADE, verbose_name="Автор", related_name='books_set')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name='books_set')
    name = models.CharField(max_length=200, verbose_name="Название книги")
    annotation = models.TextField(verbose_name="Аннотация")
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    amount = models.PositiveIntegerField(verbose_name="Количество")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

class Model(models.Model):
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"


class EBooks(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель", related_name='ebooks_set')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name="Модель", related_name='ebooks_set')
    country = models.CharField(max_length=50, verbose_name="Страна производства")
    article_number = models.IntegerField(verbose_name="Артикул")
    amount = models.PositiveIntegerField(verbose_name="Количество")
    features = models.TextField(verbose_name="Описание")
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

    class Meta:
        verbose_name = "Электронная книга"
        verbose_name_plural = "Электронные книги"


class EBooks_other_shops(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название магазинов")
    ebooks = models.ManyToManyField(EBooks, related_name='ebookshops', verbose_name="Электронные книги")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Другой магазин эл. книг"
        verbose_name_plural = "Другие магазины эл.книг"


class OfficeSupplies(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Производитель")
    country_manufacturer = models.CharField(max_length=50, verbose_name="Страна происхождения")
    article_number = models.IntegerField(verbose_name="Артикул")
    manufactured_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата изготовления", blank=True)
    amount = models.IntegerField(verbose_name="Количество")
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    class Meta:
        verbose_name_plural = "Офисные принадлежности"

class Pen(OfficeSupplies):
    office_supplies = models.OneToOneField(OfficeSupplies, on_delete=models.CASCADE, primary_key=True, related_name='pen_set')

    class Meta:
        verbose_name = "Ручка"
        verbose_name_plural = "Ручки"

class Pencil(OfficeSupplies):
    office_supplies = models.OneToOneField(OfficeSupplies, on_delete=models.CASCADE, primary_key=True, related_name='pencil_set')

    class Meta:
        verbose_name = "Карандаш"
        verbose_name_plural = "Карандаши"

class Paper(OfficeSupplies):
    office_supplies = models.OneToOneField(OfficeSupplies, on_delete=models.CASCADE, primary_key=True, related_name='paper_set')

    class Meta:
        verbose_name = "Бумага"
        verbose_name_plural = "Бумага"

class Notebook(OfficeSupplies):
    office_supplies = models.OneToOneField(OfficeSupplies, on_delete=models.CASCADE, primary_key=True, related_name='notebook_set')

    class Meta:
        verbose_name = "Блокнот"
        verbose_name_plural = "Блокноты"

class Clip(OfficeSupplies):
    office_supplies = models.OneToOneField(OfficeSupplies, on_delete=models.CASCADE, primary_key=True, related_name='clip_set')

    class Meta:
        verbose_name = "Скрепка"
        verbose_name_plural = "Скрепки"

class Envelope(OfficeSupplies):
    office_supplies = models.OneToOneField(OfficeSupplies, on_delete=models.CASCADE, primary_key=True, related_name='envelope_set')

    class Meta:
        verbose_name = "Конверт"
        verbose_name_plural = "Конверты"

class Paint(OfficeSupplies):
    office_supplies = models.OneToOneField(OfficeSupplies, on_delete=models.CASCADE, primary_key=True, related_name='paint_set')

    class Meta:
        verbose_name_plural = "Краски для рисования"

class Marker(OfficeSupplies):
    office_supplies = models.OneToOneField(OfficeSupplies, on_delete=models.CASCADE, primary_key=True, related_name='marker_set')

    class Meta:
        verbose_name = "Маркер"
        verbose_name_plural = "Маркеры"