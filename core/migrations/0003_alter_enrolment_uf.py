# Generated by Django 3.2 on 2021-05-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_enrolment_uf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolment',
            name='uf',
            field=models.ManyToManyField(to='core.UF'),
        ),
    ]
