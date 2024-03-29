import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .item import Item


class Account(models.Model):
    """
    A User has many Accounts but an Account has only one User.
    An Account has many Transactions but a Transaction can have only one Account.
    An Item has one Account and an Account has only on Item.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    account_id = models.CharField(_("account id"), max_length=50)
    mask = models.CharField(_("mask"), max_length=4)
    name = models.CharField(_("name"), max_length=100)
    subtype = models.CharField(_("subtype"), max_length=50)
    type = models.CharField(_("type"), max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )
    item = models.OneToOneField(
        Item, on_delete=models.CASCADE, related_name="account", verbose_name=_("item")
    )
    date_created = models.DateTimeField(_("date created"), default=timezone.now)

    class Meta:
        db_table = "api_plaid_account"
        indexes = [models.Index(fields=["account_id"])]
        verbose_name_plural = "accounts"

    def __str__(self):
        return self.name.title()

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
