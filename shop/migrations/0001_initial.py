# Generated by Django 4.0.2 on 2022-02-14 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('catagory_img', models.ImageField(upload_to='shop/images/catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('Product_img', models.ImageField(upload_to='shop/images/Product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_active', models.BooleanField(default=True)),
                ('is_stock', models.BooleanField(default=True)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('catagory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product_catagory', to='shop.catagory')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
