from django.db import models
import django.utils.timezone as timezone
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


class Term(models.Model):
    class Meta:
        verbose_name = "Curs"
        verbose_name_plural = "Cursos"
    name = models.CharField("nom", max_length=200)
    desc = models.TextField(
        "descripció", max_length=255, blank=True, null=True)
    start = models.DateField("data inici", null=False)
    end = models.DateField("data finalització", null=True, default=None)
    active = models.BooleanField("és actiu", default=False)

    def __str__(self):
        return self.name


class Career(models.Model):
    class Meta:
        verbose_name = "Cicle"
        verbose_name_plural = "Cicles"
    name = models.CharField("nom", max_length=200)
    code = models.CharField("codi", max_length=20)
    desc = models.TextField(
        "descripció", max_length=300, blank=True, null=True)
    hours = models.IntegerField("duracio", null=False, default=0)
    start = models.DateField("data inici", null=False, default=timezone.now)
    end = models.DateField("data finalització", null=True, default=None)
    active = models.BooleanField("és actiu", default=False)
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ProfileRequirement(models.Model):
    class Meta:
        verbose_name = "Perfil de requeriments"
        verbose_name_plural = "Perfils de requeriment"
    name = models.CharField("nom", max_length=50)
    description = models.TextField("descripció", null=True)

    def __str__(self):
        return self.name


class MP(models.Model):
    class Meta:
        verbose_name_plural = "MPs"
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    desc = models.TextField(blank=True, null=True)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UF(models.Model):
    class Meta:
        verbose_name_plural = "UFs"
    CHOICES = (
        ('1', 'Primer'),
        ('2', 'Segon'),
    )
    name = models.CharField("nom", max_length=255)
    code = models.CharField("codi", max_length=20)
    course = models.CharField(
        "primer o segon", max_length=20, choices=CHOICES, default=None, null=True)
    desc = models.CharField(
        "descripcio", max_length=300, blank=True, null=True)
    price = models.IntegerField("preu", default=25)
    mp = models.ForeignKey(MP, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField("és actiu", default=True)

    def __str__(self):
        return self.name


class ProfileRequirement(models.Model):

    class Meta:
        verbose_name = "Perfil de requeriments"
        verbose_name_plural = "Perfils de requeriment"
    CHOICES = (
        ('EX', 'Exempció'),
        ('BO', 'Bonificació'),
        ('MA', 'Obligatori')
    )


    name = models.CharField("nom", max_length=255)
    description = models.TextField("descripció", null=True)
    profile_type = models.CharField('profile_type', max_length=20, choices=CHOICES, default=None, null=True, blank=True)
    """ Remember to make non nullable on production """

    def __str__(self):
        return self.name


class Enrolment(models.Model):
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matricules"

    CHOICES = (
        ('P', 'Pendent'),
        ('V', 'Validat'),
        ('R', 'Rebutjat'),
        ('B', 'Buit')
    )
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    uf = models.ManyToManyField(UF)
    dni = models.CharField("dni", max_length=30)
    state = models.CharField("estat de matrícula",
                             max_length=20, choices=CHOICES, default=None)
    birthplace = models.CharField(
        "lloc de naixement", max_length=50, null=True, default=None)
    birthday = models.DateField("data de naixement", null=True, default=None)
    address = models.CharField("adreça", max_length=255, null=True)
    city = models.CharField("ciutat", max_length=150, null=True)
    postal_code = models.CharField("codi postal", null=True, max_length=5)
    phone_number = models.CharField(
        "número de telèfon", null=True, max_length=14)
    email = models.EmailField("correu", max_length=254, null=True)
    emergency_number = models.CharField(
        "número d'emergència", null=True, max_length=14)
    tutor_1_dni = models.CharField(
        "dni del pare/mare o tutor/a legal", max_length=30, null=True, default=None)
    tutor_1_name = models.CharField(
        "nom del pare/mare o tutor/a legal (2)", max_length=50, null=True, default=None)
    tutor_1_lastname1 = models.CharField(
        "cognoms del pare/mare o tutor/a legal (2)", max_length=50, null=True, default=None)
    tutor_1_lastname2 = models.CharField(
        "cognoms del pare/mare o tutor/a legal (2)", max_length=50, null=True, default=None)
    tutor_2_dni = models.CharField(
        "dni del pare/mare o tutor/a legal (2)", max_length=9, null=True, default=None)
    tutor_2_name = models.CharField(
        "cognoms del pare/mare o tutor/a legal (2)", max_length=50, null=True, default=None)
    tutor_2_lastname1 = models.CharField(
        "cognoms del pare/mare o tutor/a legal (2)", max_length=50, null=True, default=None)
    tutor_2_lastname2 = models.CharField(
        "cognoms del pare/mare o tutor/a legal (2)", max_length=50, null=True, default=None)
    image_rights = models.BooleanField("Drets d'imatge", null=True)
    excursions = models.BooleanField("Salides d'excursio", null=True)
    extracurricular = models.BooleanField("Salides extraescolars", null=True)
    profile_req = models.ForeignKey(
        ProfileRequirement, on_delete=models.SET_NULL, null=True)
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True)
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, null=True
    )
    
    def __str__(self):
        return self.email


class Record(models.Model):
    uf = models.ForeignKey(UF, on_delete=models.SET_NULL, null=True)
    uf_name = models.CharField(
        verbose_name="nom de la unitat formativa", max_length=80)
    uf_code = models.CharField(
        verbose_name="codi de la unitat formativa", max_length=12)
    student_id = models.CharField(
        verbose_name="DNI de l'estudiant", max_length=30)
    term = models.CharField(verbose_name="any escolar", max_length=50)
    career_code = models.CharField(
        verbose_name="codi del cicle formatiu", max_length=12)


class Requirement(models.Model):
    verbose_name = "Requeriment"
    verbose_name_plural = "Requeriments"

    class Meta:
        verbose_name = "Requeriment"

    profile = models.ForeignKey(
        ProfileRequirement, on_delete=models.SET_NULL, null=True)
    name = models.CharField("nom", max_length=255)

    def __str__(self):
        return self.name


class Req_enrol(models.Model):
    class Meta:
        verbose_name = "Requeriments matricula"

    CHOICES = (
        ('P', 'Pendent'),
        ('V', 'Validat'),
        ('R', 'Rebutjat'),
        ('B', 'Buit')
    )
    requirement = models.ForeignKey(
        Requirement, on_delete=models.SET_NULL, null=True)
    enrolment = models.ForeignKey(
        Enrolment, on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=20, choices=CHOICES, default=None)


class Upload(models.Model):
    class Meta:
        verbose_name = "Pujades"
        verbose_name_plural = "Pujades"
    data = models.FileField(upload_to="uploads/", null=True, blank=True)
    req_enrol = models.ForeignKey(
        Req_enrol, on_delete=models.SET_NULL, null=True)
