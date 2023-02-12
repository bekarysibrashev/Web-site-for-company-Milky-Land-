# Generated by Django 4.1.2 on 2022-12-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_products_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('description', models.TextField()),
            ],
        ),
    ]
