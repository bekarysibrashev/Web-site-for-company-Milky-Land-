# Generated by Django 4.1.2 on 2023-01-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_alter_products_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('carouselImg', models.ImageField(upload_to='')),
            ],
        ),
    ]
