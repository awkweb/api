import uuid
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Institution(models.Model):
    """
    Institutions have many Items but an Item has only one Institution.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    color = models.CharField(_("color"), max_length=6)
    institution_id = models.CharField(
        _("institution id"), max_length=50, default="ffffff"
    )
    name = models.CharField(_("name"), max_length=100)
    date_created = models.DateTimeField(_("date created"), default=timezone.now)

    class Meta:
        db_table = "api_plaid_institution"
        indexes = [models.Index(fields=["institution_id"])]
        verbose_name_plural = "institutions"

    def __str__(self):
        return self.name.title()
