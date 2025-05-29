from django.urls import path

from api.views import WebhookView, BalanceView

urlpatterns = [
    path("webhook/bank/", WebhookView.as_view(), name="webhook"),
    path("organizations/<str:inn>/balance/", BalanceView.as_view(), name="balance"),
]
