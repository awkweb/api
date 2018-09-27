import uuid
from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .institution import Institution


class Item(models.Model):
    """
    A User has many Items but an Item has only one User.
    An Item has many Accounts but an Account has only one Item.
    Institutions have many Items but an Item has only one Institution.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    access_token = models.CharField(_("access_token"), max_length=100)
    item_id = models.CharField(_("item_id"), max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, verbose_name=_("institution")
    )
    date_created = models.DateTimeField(_("date_created"), default=timezone.now)

    class Meta:
        db_table = "api_plaid_item"
        indexes = [models.Index(fields=["item_id"])]
        verbose_name = "item"
        verbose_name_plural = "items"

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return request.user == self.user

    @staticmethod
    def has_write_permission(self):
        return True

    def has_object_write_permission(self, request):
        return request.user == self.user
