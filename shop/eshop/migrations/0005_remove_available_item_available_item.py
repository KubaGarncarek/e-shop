# Generated by Django 4.0.5 on 2022-08-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_remove_available_item_available_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='available',
            name='item',
        ),
        migrations.AddField(
            model_name='available',
            name='item',
            field=models.ManyToManyField(related_name='available_produkcts', to='eshop.item'),
        ),
    ]
