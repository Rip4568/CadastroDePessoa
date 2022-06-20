from django.db import models
from django.urls import reverse

# Create your models here.

class Pessoa(models.Model):

    

    class Meta:
        verbose_name = _("pessoa")
        verbose_name_plural = _("pessoas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pessoa_detail", kwargs={"pk": self.pk})
