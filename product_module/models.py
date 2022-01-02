# product_module/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural = 'دسته بندی‌ها'


class ProductCode(models.Model):
    code = models.CharField(max_length=200, verbose_name='کد')

    def __str__(self):
        return f"{self.code}"
    
    class Meta:
        verbose_name='کد محصول'
        verbose_name_plural = 'کدهای محصولات'


class Product(models.Model):
    title = models.CharField(max_length=300)
    product_code = models.OneToOneField(
        to=ProductCode,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='product_Code',
        verbose_name='کد محصول'
    )
    category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.CASCADE,
        null=True,
        related_name='products',
        verbose_name='دسته بندی'
    )
    price = models.IntegerField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0
    )
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name='محصول'
        verbose_name_plural = 'محصولات'
