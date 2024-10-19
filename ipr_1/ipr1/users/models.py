from datetime import date

from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from PIL import Image


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Измените имя для обратной ссылки
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Измените имя для обратной ссылки
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def is_adult(self):
        """Проверяет, является ли пользователь совершеннолетним."""
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age >= 18
        return False


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)