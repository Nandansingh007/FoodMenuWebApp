# Generated by Django 4.2.4 on 2023-09-05 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alter_item_item_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_images',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/1147/1147805.png', max_length=500),
        ),
    ]
