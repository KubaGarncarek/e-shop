# Generated by Django 4.0.5 on 2022-08-09 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0005_remove_available_item_available_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='available',
            old_name='count',
            new_name='count_of_size',
        ),
        migrations.RemoveField(
            model_name='available',
            name='size',
        ),
        migrations.RemoveField(
            model_name='available',
            name='item',
        ),
        migrations.AddField(
            model_name='available',
            name='item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='eshop.item'),
            preserve_default=False,
        ),
    ]
