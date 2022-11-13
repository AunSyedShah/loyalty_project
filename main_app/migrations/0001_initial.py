# Generated by Django 4.1.3 on 2022-11-05 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=100)),
                ('product_price', models.FloatField(default=0)),
                ('loyalty_points', models.IntegerField(default=0)),
                ('product_image', models.ImageField(default='', upload_to='product_images')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=100)),
                ('loyalty_points', models.IntegerField(default=0)),
                ('products', models.ManyToManyField(blank=True, to='main_app.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
