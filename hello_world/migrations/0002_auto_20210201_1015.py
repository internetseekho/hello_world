# Generated by Django 3.1.5 on 2021-02-01 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table_2',
            old_name='table_1_id',
            new_name='table_2_id',
        ),
        migrations.AlterModelTable(
            name='table_1',
            table='table_1',
        ),
        migrations.AlterModelTable(
            name='table_2',
            table='table_2',
        ),
    ]