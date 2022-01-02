# Generated by Django 3.2 on 2022-01-02 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='تیتر')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / حذف نشده')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال/غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / حذف نشده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی\u200cها',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=100, verbose_name='برچسب')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='product_module.product', verbose_name='برچسب\u200cهای محصول')),
            ],
            options={
                'verbose_name': 'برچسب محصول',
                'verbose_name_plural': 'برچسب محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='product_module.ProductCategory', verbose_name='دسته بندی\u200cها'),
        ),
    ]
