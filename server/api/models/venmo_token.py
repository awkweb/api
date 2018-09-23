from django.conf import settings
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class VenmoToken(models.Model):
    """
    A User has many VenmoTokens but a VenmoToken has only one User.
    """

    value = models.CharField(_("value"), max_length=100)
    venmo_username = models.CharField(_("venmo_username"), max_length=100)
    user = models.ForeignKey(
        _("user"), settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "venmo tokens"
