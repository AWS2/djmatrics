# Generated by Django 3.2 on 2021-05-11 15:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nom')),
                ('code', models.CharField(max_length=20, verbose_name='codi')),
                ('desc', models.TextField(blank=True, max_length=300, null=True, verbose_name='descripció')),
                ('hours', models.IntegerField(default=0, verbose_name='duracio')),
                ('start', models.DateField(default=django.utils.timezone.now, verbose_name='data inici')),
                ('end', models.DateField(default=None, null=True, verbose_name='data finalització')),
                ('active', models.BooleanField(default=False, verbose_name='és actiu')),
            ],
            options={
                'verbose_name': 'Cicle',
                'verbose_name_plural': 'Cicles',
            },
        ),
        migrations.CreateModel(
            name='Enrolment',
            fields=[
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to='auth.user')),
                ('dni', models.CharField(max_length=30, verbose_name='dni')),
                ('state', models.CharField(choices=[('P', 'Pendent'), ('V', 'Validat'), ('R', 'Rebutjat'), ('B', 'Buit')], default=None, max_length=20, verbose_name='estat de matrícula')),
                ('birthplace', models.CharField(default=None, max_length=50, null=True, verbose_name='lloc de naixement')),
                ('birthday', models.DateField(default=None, null=True, verbose_name='data de naixement')),
                ('address', models.CharField(max_length=255, verbose_name='adreça')),
                ('city', models.CharField(max_length=150, verbose_name='ciutat')),
                ('postal_code', models.CharField(max_length=5, verbose_name='codi postal')),
                ('phone_number', models.CharField(max_length=14, verbose_name='número de telèfon')),
                ('email', models.EmailField(max_length=255, verbose_name='correu')),
                ('emergency_number', models.CharField(max_length=14, verbose_name="número d'emergència")),
                ('tutor_1', models.CharField(default=None, max_length=50, null=True, verbose_name='nom del pare/mare o tutor/a legal')),
                ('tutor_2', models.CharField(default=None, max_length=50, null=True, verbose_name='nom del pare/mare o tutor/a legal (2)')),
                ('tutor_1_dni', models.CharField(default=None, max_length=30, null=True, verbose_name='dni del pare/mare o tutor/a legal')),
                ('tutor_2_dni', models.CharField(default=None, max_length=30, null=True, verbose_name='dni del pare/mare o tutor/a legal (2)')),
                ('tutor_1_name', models.CharField(default=None, max_length=50, null=True, verbose_name='nom del pare/mare o tutor/a legal (2)')),
                ('tutor_1_lastname1', models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)')),
                ('tutor_1_lastname2', models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)')),
                ('tutor_2_name', models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)')),
                ('tutor_2_lastname1', models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)')),
                ('tutor_2_lastname2', models.CharField(default=None, max_length=50, null=True, verbose_name='cognoms del pare/mare o tutor/a legal (2)')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.career')),
            ],
            options={
                'verbose_name': 'Matrícula',
                'verbose_name_plural': 'Matricules',
            },
        ),
        migrations.CreateModel(
            name='MP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20)),
                ('desc', models.TextField(blank=True, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.career')),
            ],
            options={
                'verbose_name_plural': 'MPs',
            },
        ),
        migrations.CreateModel(
            name='ProfileRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nom')),
                ('description', models.TextField(null=True, verbose_name='descripció')),
            ],
            options={
                'verbose_name': 'Perfil de requeriments',
                'verbose_name_plural': 'Perfils de requeriment',
            },
        ),
        migrations.CreateModel(
            name='Req_enrol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('P', 'Pendent'), ('V', 'Validat'), ('R', 'Rebutjat'), ('B', 'Buit')], default=None, max_length=20)),
                ('enrolment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.enrolment')),
            ],
            options={
                'verbose_name': 'Requeriments matricula',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nom')),
                ('desc', models.TextField(blank=True, max_length=255, null=True, verbose_name='descripció')),
                ('start', models.DateField(verbose_name='data inici')),
                ('end', models.DateField(default=None, null=True, verbose_name='data finalització')),
                ('active', models.BooleanField(default=False, verbose_name='és actiu')),
            ],
            options={
                'verbose_name': 'Curs',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(blank=True, null=True, upload_to='')),
                ('req_enrol', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.req_enrol')),
            ],
            options={
                'verbose_name': 'Pujades',
                'verbose_name_plural': 'Pujades',
            },
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
                ('code', models.CharField(max_length=20, verbose_name='codi')),
                ('course', models.CharField(choices=[('1', 'Primer'), ('2', 'Segon')], default=None, max_length=20, null=True, verbose_name='primer o segon')),
                ('desc', models.CharField(blank=True, max_length=300, null=True, verbose_name='descripcio')),
                ('price', models.IntegerField(default=25, verbose_name='preu')),
                ('active', models.BooleanField(default=True, verbose_name='és actiu')),
                ('mp', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.mp')),
            ],
            options={
                'verbose_name_plural': 'UFs',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.profilerequirement')),
            ],
            options={
                'verbose_name': 'Requeriment',
            },
        ),
        migrations.AddField(
            model_name='req_enrol',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.requirement'),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf_name', models.CharField(max_length=80, verbose_name='nom de la unitat formativa')),
                ('uf_code', models.CharField(max_length=12, verbose_name='codi de la unitat formativa')),
                ('student_id', models.CharField(max_length=30, verbose_name="DNI de l'estudiant")),
                ('term', models.CharField(max_length=50, verbose_name='any escolar')),
                ('career_code', models.CharField(max_length=12, verbose_name='codi del cicle formatiu')),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.uf')),
            ],
        ),
        migrations.AddField(
            model_name='enrolment',
            name='profile_req',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.profilerequirement'),
        ),
        migrations.AddField(
            model_name='enrolment',
            name='uf',
            field=models.ManyToManyField(to='core.UF'),
        ),
        migrations.AddField(
            model_name='career',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.term'),
        ),
    ]
