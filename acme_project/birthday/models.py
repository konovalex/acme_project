from django.db import models
from django.urls import reverse

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Фамилия',
        help_text='Необязательное поле'
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        validators=(real_age,)
    )
    image = models.ImageField(
        blank=True,
        upload_to='birthdays_images',
        verbose_name='Фото'
    )

    class Meta:
        verbose_name = 'день рождения'
        verbose_name_plural = 'Дни рождения'
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return (self.first_name + ' '
                + self.last_name + ' ('
                + str(self.birthday) + ')')
