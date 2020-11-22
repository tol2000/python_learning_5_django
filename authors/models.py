from django.db import models


class Author(models.Model):

    class Meta:
        verbose_name = 'Аффтар'
        verbose_name_plural = 'Аффтары'

    LEVELS = (
        ('J', 'Junior'),
        ('M', 'Middle'),
        ('S', 'Senior')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, default='none@no.no', blank='')
    level = models.CharField(max_length=1, choices=LEVELS)

    def __str__(self):
        return (
            f'{self.pk:0>5}. Аффтар {self.first_name} {self.last_name}' +
            (f' АКА {self.email}' if self.email else ' with no email')
        )
