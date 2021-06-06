# Generated by Django 3.2 on 2021-06-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210606_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': 'UF_superada', 'verbose_name_plural': 'UFs_superades'},
        ),
        migrations.AlterModelOptions(
            name='req_enrol',
            options={'verbose_name': 'Requeriment matricula'},
        ),
        migrations.AddField(
            model_name='req_enrol',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requirement',
            name='description',
            field=models.TextField(null=True, verbose_name='descripció'),
        ),
    ]
