from django.db import models


class Author(models.Model):

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)

    def __str__(self):
        return (
            f'Аффтар {self.first_name} {self.last_name}' +
            (f' АКА {self.email}' if self.email else ' with no email')
        )
