from django.db import models

class Exemple(models.Model):
    obsolete = models.BooleanField(u"nom complet", default=True)
    name = models.CharField(u"Nom", max_length=32)

    class Meta:
        verbose_name = u"Example de modele"

    def __unicode__(self):
        return self.name + "(obsolete)" if self.obsolete else ""

# Create your models here.
