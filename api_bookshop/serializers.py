from rest_framework import serializers
from bookshop.models import (Category,
                            Authors,
                            Books,
                            Manufacturer,
                            Model,
                            EBooks,
                            EBooks_other_shops,
                            OfficeSupplies,
                            Pen,
                            Pencil,
                            Paper,
                            Notebook,
                            Clip,
                            Envelope,
                            Paint,
                            Marker
                            )

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name_category = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name_category = validated_data.get('name_category', instance.name_category)
        instance.save()
        return instance

class AuthorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name_authors = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Authors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name_authors = validated_data.get('name_authors', instance.name_authors)
        instance.save()
        return instance

class BooksSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    writer = serializers.PrimaryKeyRelatedField(queryset=Authors.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    name = serializers.CharField(max_length=200)
    annotation = serializers.CharField(required=False)
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    amount = serializers.IntegerField()

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.writer = validated_data.get('writer', instance.writer)
        instance.category = validated_data.get('category', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.annotation = validated_data.get('annotation', instance.annotation)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.price = validated_data.get('price', instance.price)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance

class ManufacturerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Manufacturer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer_name = validated_data.get('manufacturer_name', instance.manufacturer_name)
        instance.save()
        return instance

class ModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.model_name = validated_data.get('model_name', instance.model_name)
        instance.save()
        return instance

class EBooksSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())
    model = serializers.PrimaryKeyRelatedField(queryset=Model.objects.all())
    country = serializers.CharField(max_length=50)
    article_number = serializers.IntegerField()
    amount = serializers.IntegerField()
    features = serializers.CharField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return EBooks.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.model = validated_data.get('model', instance.model)
        instance.country =validated_data.get('country', instance.country)
        instance.article_number = validated_data.get('article_number', instance.article_number)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.features = validated_data.get('features', instance.features)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class EBooks_other_shopsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    ebooks = serializers.PrimaryKeyRelatedField(queryset=EBooks.objects.all(), many=True)

    def create(self, validated_data):
        return EBooks_other_shops.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.ebooks = validated_data.get('ebooks', instance.ebooks)
        instance.save()
        return instance

class OfficeSuppliesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=50)
    country_manufacturer = serializers.CharField(max_length=50)
    article_number = serializers.IntegerField()
    manufactured_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    amount = serializers.IntegerField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return OfficeSupplies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.brand)
        instance.country_manufacturer = validated_data.get('country_manufacturer', instance.country_manufacturer)
        instance.article_number = validated_data.get('article_number', instance.article_number)
        instance.manufactured_date = validated_data.get('manufactured_date', instance.manufactured_date)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class PenSerializer(OfficeSuppliesSerializer):
    office_supplies = serializers.PrimaryKeyRelatedField(queryset=OfficeSupplies.objects.all())

class PencilSerializer(OfficeSuppliesSerializer):
    office_supplies = serializers.PrimaryKeyRelatedField(queryset=OfficeSupplies.objects.all())

class PaperSerializer(OfficeSuppliesSerializer):
    office_supplies = serializers.PrimaryKeyRelatedField(queryset=OfficeSupplies.objects.all())

class NotebookSerializer(OfficeSuppliesSerializer):
    office_supplies = serializers.PrimaryKeyRelatedField(queryset=OfficeSupplies.objects.all())

class ClipSerializer(OfficeSuppliesSerializer):
    office_supplies = serializers.PrimaryKeyRelatedField(queryset=OfficeSupplies.objects.all())

class EnvelopeSerializer(OfficeSuppliesSerializer):
    office_supplies = serializers.PrimaryKeyRelatedField(queryset=OfficeSupplies.objects.all())

class PaintSerializer(OfficeSuppliesSerializer):
    office_supplies = serializers.PrimaryKeyRelatedField(queryset=OfficeSupplies.objects.all())

class MarkerSerializer(OfficeSuppliesSerializer):
    office_supplies = serializers.PrimaryKeyRelatedField(queryset=OfficeSupplies.objects.all())


