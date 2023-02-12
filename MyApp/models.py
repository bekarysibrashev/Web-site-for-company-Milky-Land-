from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, default="rerere") 

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=100, default="news") 
    img = models.ImageField()
    description = models.CharField(max_length= 400)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=280)
    img = models.ImageField()
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    url = models.SlugField()
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title



class Info(models.Model):
    title = models.CharField(max_length=300)
    file = models.FileField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Файлы сайта (Видео)'
        verbose_name_plural = 'Файлы сайта (Видео)'

    def __str__(self):
        return self.title
# Create your models here.




class Carusel(models.Model):
    carusel = models.CharField(max_length=100 ,default="Слайдер")

    class Meta:
        verbose_name = 'Слайдер(Стопка)'
        verbose_name_plural = 'Слайдеры(Стопка)'


class ImagesOfCarusel(models.Model):
    title = models.CharField(max_length=100, default="img")
    carouselImg = models.ImageField()
    relation = models.ForeignKey(Carusel, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Фото для слайдеров'
        verbose_name_plural = 'Фото для слайдеров'

    def __str__(self):
        return self.title   