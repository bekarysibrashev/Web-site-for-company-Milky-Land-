# Generated by Django 4.1.2 on 2023-01-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_remove_carusel_carouselimg_remove_carusel_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carusel',
            name='img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]