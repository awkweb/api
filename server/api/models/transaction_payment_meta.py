from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class TransactionPaymentMeta(models.Model):
    """
    A Transaction can have only one TransactionPaymentMeta and a TransactionPaymentMeta can have only one Transaction.
    """

    reference_number = models.CharField(_("reference_number"), max_length=50)
    ppd_id = models.CharField(_("ppd_id"), max_length=50)
    payee_name = models.CharField(_("payee_name"), max_length=50)

    class Meta:
        verbose_name_plural = "transaction payment meta"
