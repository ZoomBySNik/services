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


class CustomUser(AbstractUser):
    GENDERS = (
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский')
    )
    middle_name = models.CharField("Отчество", max_length=50, null=True, blank=True)
    gender = models.CharField("Пол", max_length=10, choices=GENDERS, default='')

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class PriceList(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
    ]
    number = models.CharField(max_length=20, verbose_name='Номер')
    approval_date = models.DateField(verbose_name='Дата утверждения')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')

    def __str__(self):
        return '%s' % (self.number)

    class Meta:
        verbose_name = 'Прайслист'
        verbose_name_plural = 'Прайслисты'


class PriceListPosition(models.Model):
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE, verbose_name='Прайслист')
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE, verbose_name='Платье')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return '%s' % (self.price_list)

    class Meta:
        verbose_name = 'Позиция прайслиста'
        verbose_name_plural = 'Позиции прайслистов'


class Customer(models.Model):
    first_name = models.CharField(max_length=120, verbose_name='Имя')
    second_name = models.CharField(max_length=120, verbose_name='Фамилия')
    last_name = models.CharField(max_length=120, verbose_name='Отчество')
    phone_number = models.CharField(max_length=18, verbose_name='Номер телефона')
    adress = models.CharField(max_length=120, verbose_name='Адрес')
    email_adress = models.EmailField(verbose_name='Адрес')

    def __str__(self):
        return '%s' % (self.first_name)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class RecordingForFitting(models.Model):
    date_of_fitting = models.DateField(verbose_name='Дата примерки')
    time_of_fitting = models.TimeField(verbose_name='Время примерки')
    status = models.CharField(max_length=20, verbose_name='Статус')
    commentary = models.TextField(verbose_name='Комментарий')
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE, verbose_name='Платье')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return '%s' % (self.date_of_fitting)

    class Meta:
        verbose_name = 'Запись на примерку'
        verbose_name_plural = 'Записи на примерки'