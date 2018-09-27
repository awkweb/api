from rest_framework import mixins
from rest_framework import viewsets


class DestroyListViewSet(
    mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    A viewset that provides `destroy` and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass
