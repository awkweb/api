from django.conf.urls import url, include
from rest_framework import routers
from ..api import views


router = routers.DefaultRouter()
router.register(r"budgets", views.BudgetViewSet, base_name="budgets")
router.register(r"transactions", views.TransactionViewSet, base_name="transactions")
router.register(r"items", views.ItemViewSet, base_name="items")
router.register(r"users", views.UserViewSet, base_name="users")

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^items/hooks", views.handle_plaid_hook),
    url(r"^auth/password/change/", views.ChangePasswordView.as_view()),
    url(r"^auth/login/", views.LoginView.as_view()),
    url(r"^auth/logout/", views.LogoutView.as_view()),
    url(r"^auth/register/", views.RegisterView.as_view()),
    url(r"^auth-api/", include("rest_framework.urls", namespace="rest_framework")),
]
