from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()
# Create your models here.


class category(models.Model):       #   category table / таб категорий 

    title = models.CharField(verbose_name='Название категории', max_length=255)
    slug = models.SlugField(verbose_name='Артикул', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'




class sub_category(models.Model):       #   sub_category list / таб подкатегорий

    category = models.ForeignKey(category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Подкатегория', max_length=100)
    slug = models.SlugField(verbose_name='Артикул', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("sub_category", kwargs={"sub_category_slug": self.slug})

    class Meta:
        verbose_name = 'Подкатегории'
        verbose_name_plural = 'Подкатегории'




class collection(models.Model):      #   collection list / список коллекций

    category = models.ForeignKey(category, verbose_name='Категория', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(sub_category, verbose_name="Подкатегория", on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название коллекции', max_length=100) 
    slug = models.SlugField(verbose_name='Артикул', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("collection", kwargs={"collection_slug": self.slug})

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
    
    


class catalog(models.Model):        #   catalog list / список товара

    category = models.ForeignKey(category, verbose_name='Категория', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(sub_category, verbose_name="Подкатегория", on_delete=models.CASCADE, null=True, blank=True)
    collection = models.ForeignKey(collection, verbose_name="Коллекция", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(verbose_name='Артикул', unique=True)
    price = models.CharField(verbose_name='Цена', max_length=20)
    max_price = models.CharField(verbose_name='Цена за комплект (необязательно)', max_length=20, blank=True)
    image = models.ImageField(verbose_name='Основное фото')
    second_image = models.ImageField(verbose_name='доп фото (необязательно)', blank=True)
    sub_name = models.TextField(verbose_name='Описание / назваие коллекции')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
    
    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'




class Sizes(models.Model):      #   size ticets / таб заявок для замеров
    
    f_name = models.CharField(verbose_name='Имя', max_length=50)
    l_name = models.CharField(verbose_name='Отчество', max_length=50)
    phone = models.CharField(verbose_name='Номер телефона', max_length=15)

    def __str__(self):
        return '{} {}'.format(self.f_name, self.l_name)




class Furnite_category(models.Model):       #   furnite categories / категории фурнитуры

    title = models.CharField(verbose_name='Название', max_length=50)
    slug = models.SlugField(verbose_name='Артикул', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("furnite_category", kwargs={"furnite_category_slug": self.slug})

    class Meta:
        verbose_name = 'Категория фурнитуры'
        verbose_name_plural = 'Категории фурнитуры'

    
    


class Furnite_sub_category(models.Model):       #   furnite sub_category / подкатегории фурнитуры
   
    category = models.ForeignKey(Furnite_category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Подкатегория', max_length=100)
    slug = models.SlugField(verbose_name='Артикул', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("furnite_subcategory", kwargs={"furnite_subcategory_slug": self.slug})

    class Meta:
        verbose_name = 'Подкатегория фурнитуры'
        verbose_name_plural = 'Подкатегории фурнитуры'    




class Furnite(models.Model):        #   furnite catalog list / список фурнитуры
    
    category = models.ForeignKey(Furnite_category, verbose_name='Категория', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Furnite_sub_category, verbose_name="Подкатегория", on_delete=models.CASCADE,)
    title = models.CharField(verbose_name='Название', max_length=50)
    image = models.ImageField()
    dist = models.TextField(verbose_name='Описание / назваие коллекции')
    price = models.CharField(verbose_name='Цена', max_length=20)
    slug = models.SlugField(verbose_name='Артикул', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("furnite", kwargs={"furnite_slug": self.slug})

    class Meta:
        verbose_name = 'Фурнитура'
        verbose_name_plural = 'Фурнитура'




class News(models.Model):       #   news tab / Новости

    title = models.CharField(verbose_name='Загаловок', max_length=50)
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



class Orders(models.Model):

    first_name = models.CharField(verbose_name='Имя', max_length=30)
    Middle_name = models.CharField(verbose_name='Отчество', max_length=30)
    Phone = models.CharField(verbose_name='Номер телефона', max_length=15)
    Address = models.TextField(verbose_name='Адрес')
    Cart = models.TextField(verbose_name='Корзина')
    Date = models.DateTimeField(verbose_name='Дата заявки', auto_now_add=True)

    def __str__(self):
        return self.Address

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'