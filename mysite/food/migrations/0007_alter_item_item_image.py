# Generated by Django 4.2.4 on 2023-09-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_rename_item_images_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(max_length=500),
        ),
    ]