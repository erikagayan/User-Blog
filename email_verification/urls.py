from django.urls import path
from .views import EmailVerificationView, EmailResultView


urlpatterns = [
    path("verify-email/", EmailVerificationView.as_view(), name="verify-email"),
    path("email-result/", EmailResultView.as_view(), name="email-result"),
]


app_name = "email"
