# product_module/models.py
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(
        max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(
        max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی‌ها'


class ProductBrand(models.Model):
    title = models.CharField(
        max_length=300, db_index=True, verbose_name='نام برند')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    category = models.ManyToManyField(
        to=ProductCategory,
        related_name='products',
        verbose_name='دسته بندی‌ها'
    )
    brand = ForeignKey(
        to=ProductBrand,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='brand',
        verbose_name='برند'
    )
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(
        max_length=360,
        db_index=True,
        null=True,
        verbose_name='توضیحات کوتاه'
    )
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(
        max_length=200,
        default="",
        null=False,
        db_index=True,
        blank=True,
        unique=True,
        verbose_name='عنوان در url'
    )
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTag(models.Model):
    caption = models.CharField(
        max_length=100, db_index=True, verbose_name='برچسب')
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_tags',
        verbose_name='برچسب‌های محصول'
    )

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'برچسب محصول'
        verbose_name_plural = 'برچسب محصولات'
