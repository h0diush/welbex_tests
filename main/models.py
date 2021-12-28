from django.db import models


class BaseModel(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=155)
    qty = models.PositiveIntegerField(default=1)
    distance = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'
        ordering = ['-date']

    def __str__(self):
        return self.name
