# product_module/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class ProductTag(models.Model):
    tag = models.CharField(max_length=100, verbose_name='برچسب')

    def __str__(self):
        return self.tag
    
    class Meta:
        verbose_name='برچسب محصول'
        verbose_name_plural = 'برچسب محصولات'


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
    title=models.CharField(max_length=300, verbose_name='تیتر')
    product_code=models.OneToOneField(
        to=ProductCode,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='product',
        verbose_name='کد'
    )
    category=models.ForeignKey(
        to=ProductCategory,
        on_delete=models.CASCADE,
        null=True,
        related_name='products',
        verbose_name='دسته بندی'
    )
    product_tags=models.ManyToManyField(
        to=ProductTag,
        related_name='products',
        verbose_name='برچسب'
    )
    price=models.IntegerField(verbose_name='قیمت')
    rating=models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0,
        verbose_name='امتیاز'
    )
    short_description=models.CharField(max_length=360, null=True, verbose_name='توضیح کوتاه')
    is_active=models.BooleanField(default=False, verbose_name='فعال')
    slug=models.SlugField(default="", null=False, db_index=True, blank=True, verbose_name='اسلاگ')

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
