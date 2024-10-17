from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField, ImageField, DateField, IntegerField, FloatField, CharField, ForeignKey, PROTECT, \
    DateTimeField


class EmployeePost(models.Model):
    name = CharField(max_length=60)
    description = TextField()

    def __str__(self):
        return f'{self.name}'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(EmployeePost, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.post.name} {self.user.username}'

class FormOfArt(models.Model):
    name = CharField(max_length=60)
    description = TextField()

    def __str__(self):
        return f'{self.name}'

class Author(models.Model):
    image = ImageField(default='default.jpg', upload_to='authors_pics')
    first_name = CharField(max_length=60)
    second_name = CharField(max_length=60, blank=True, null=True)
    date_of_birth = DateField(blank=True, null=True)
    history = TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Hall(models.Model):
    name = CharField(max_length=60)
    floor = IntegerField()
    square = FloatField()

    def __str__(self):
        return f'{self.name}'

class Exposition(models.Model):
    name = CharField(max_length=60)
    image = ImageField(default='default.jpg', upload_to='exposition_pics')

    hall = models.ForeignKey(Hall, on_delete=PROTECT)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.name}'

class Exhibit(models.Model):
    name = CharField(max_length=60)
    image = ImageField(default='default.jpg', upload_to='exhibit_pics')
    year_of_creation = IntegerField(blank=True, null=True)
    description = TextField(blank=True, null=True)

    author = ForeignKey(Author, blank=True, null=True, on_delete=models.PROTECT)
    employee = ForeignKey(Employee, on_delete=models.PROTECT)
    exposition = ForeignKey(Exposition, on_delete=models.PROTECT)
    form = ForeignKey(FormOfArt, on_delete=PROTECT)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Excursion(models.Model):
    name = CharField(max_length=60)
    date_time = DateTimeField()
    image =ImageField(default='default.jpg', upload_to='exhibit_pics')

    employee = ForeignKey(Employee, on_delete=models.PROTECT)
    exposition = models.ManyToManyField(Exposition)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)