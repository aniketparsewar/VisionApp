# Generated by Django 3.0.3 on 2020-06-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyLens', '0003_auto_20200620_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelens',
            name='name',
            field=models.CharField(default='Main_Img.jpg', max_length=12),
        ),
    ]
