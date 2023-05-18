from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Cleavage(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Декольте'
        verbose_name_plural = 'Декольте'


class Sleeve(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    length_of_sleeve = models.CharField(max_length=60, verbose_name='Длина рукава')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Рукав'
        verbose_name_plural = 'Рукава'


class Skirt(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    type_of_skirt = models.CharField(max_length=60, verbose_name='Длина юбки')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Юбка'
        verbose_name_plural = 'Юбки'


class Style(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    cleavage = models.ForeignKey(Cleavage, on_delete=models.CASCADE, verbose_name='Декольте')
    sleeve = models.ForeignKey(Sleeve, on_delete=models.CASCADE, verbose_name='Рукав')
    skirt = models.ForeignKey(Skirt, on_delete=models.CASCADE, verbose_name='Юбка')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Фасон'
        verbose_name_plural = 'Фасоны'


class Brand(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Size(models.Model):
    size_russian = models.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(76)], verbose_name='Российский размер')
    size_international = models.CharField(max_length=3, verbose_name='Международный размер')

    def __str__(self):
        return '%s' % (self.size_russian)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Colour(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Material(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Dress(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Размер')
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, verbose_name='Цвет')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Материал')
    style = models.ForeignKey(Style, on_delete=models.CASCADE, verbose_name='Фасон')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Платье'
        verbose_name_plural = 'Платья'


