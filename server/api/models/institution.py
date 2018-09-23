from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Institution(models.Model):
    """
    Institutions have many PlaidTokens but an PlaidTokens has only one Institution.
    """

    institution_id = models.CharField(_("institution_id"), max_length=50)
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name_plural = "institutions"

    def __str__(self):
        return self.name.title()
