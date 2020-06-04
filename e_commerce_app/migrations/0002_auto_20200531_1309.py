# Generated by Django 3.0.6 on 2020-05-31 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('added_date', models.DateField()),
                ('image', models.ImageField(upload_to='shop/products_images')),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]
