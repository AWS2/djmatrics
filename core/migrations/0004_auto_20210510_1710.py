# Generated by Django 3.2 on 2021-05-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210510_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolment',
            name='term',
        ),
        migrations.AddField(
            model_name='enrolment',
            name='tutor_1_lastname1',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)'),
        ),
        migrations.AddField(
            model_name='enrolment',
            name='tutor_1_lastname2',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)'),
        ),
        migrations.AddField(
            model_name='enrolment',
            name='tutor_1_name',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='nom del pare/mare o tutor/a legal (2)'),
        ),
        migrations.AddField(
            model_name='enrolment',
            name='tutor_2_lastname1',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)'),
        ),
        migrations.AddField(
            model_name='enrolment',
            name='tutor_2_lastname2',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)'),
        ),
        migrations.AddField(
            model_name='enrolment',
            name='tutor_2_name',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)'),
        ),
        migrations.AddField(
            model_name='uf',
            name='course',
            field=models.CharField(choices=[('1', 'Primer'), ('2', 'Segon')], default=None, max_length=20, null=True, verbose_name='primer o segon'),
        ),
    ]
