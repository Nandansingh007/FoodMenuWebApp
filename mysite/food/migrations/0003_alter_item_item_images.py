# Generated by Django 4.2.4 on 2023-09-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_images',
            field=models.CharField(default='https://www.melbournefoodandwine.com.au/image-tools.php?w=560&h=440&src=/recipes/recipe-placeholder.jpg', max_length=500),
        ),
    ]
