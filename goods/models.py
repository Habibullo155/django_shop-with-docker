from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='name')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='slug')

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='name')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='slug')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    image = models.ImageField(upload_to="goods/", verbose_name='image', blank=True, null=True)
    description = models.TextField(verbose_name='description')
    discount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    on_stock = models.BooleanField(default=False, verbose_name='on stock')

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = "products"
        ordering = ('id',)

    def __str__(self):
        return f'{self.name} pricee- {self.price}'

    def display_id(self):
        return f'{self.id:05} '

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price
