from django.db import models


class Author(models.Model):

    objects = None

    class Meta:
        verbose_name = 'Аффтар'
        verbose_name_plural = 'Аффтары'

    LEVELS = (
        ('J', 'Junior Dev'),
        ('M', 'Middle Dev'),
        ('S', 'Senior Dev')
    )

    DICT_LEVELS = {
        x[0]: x[1] for x in LEVELS
    }

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, default='none@no.no', blank='')
    level = models.CharField(max_length=1, choices=LEVELS, default=LEVELS[0][0])

    def __str__(self):
        level_desc = self.DICT_LEVELS[self.level] if self.level else '?'
        return (
            f'{self.first_name} {self.last_name} ({level_desc})'
        )
