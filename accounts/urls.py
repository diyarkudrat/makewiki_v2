from django.urls import path
from accounts.views import SignUpView, ForgotPasswordView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='wiki-signup-page'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='wiki-forgot-password-page'),
]
