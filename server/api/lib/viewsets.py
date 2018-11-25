from rest_framework import mixins
from rest_framework import viewsets


class CreateDestroyRetrieveUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides `create`, `destroy`, `retrieve`,
    and `update` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass


class DestroyListUpdateViewSet(
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides `destroy`, `list`, and update actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass
