from rest_framework.decorators import api_view
from rest_framework.response import Response
from allauth.account.views import ConfirmEmailView
from rest_framework.views import APIView
from django.shortcuts import redirect
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from dj_rest_auth.registration.views import VerifyEmailView
from allauth.account.views import EmailVerificationSentView
from allauth.account.utils import send_email_confirmation
from django.contrib.auth import get_user_model
import os


from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)

User = get_user_model()


@api_view()
def root_route(request):
    return Response({"message": "Welcome to Memo Bubble API!"})


@api_view(["GET"])
def get_user_status(request):
    """
    Get the status of the user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: The response containing the user status and a message.

    """
    user_status = {
        "is_authenticated": request.user.is_authenticated,
        "is_staff": request.user.is_staff,
    }

    if request.user.is_staff:
        data = {"staff_status": user_status,
                "message": "You are a staff member"}
        return Response(data, status=200)
    else:
        data = {"staff_status": user_status,
                "message": "You are not a staff member"}
        return Response(data, status=200)


@api_view(["POST"])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )

    return response


class CustomConfirmEmailView(APIView, ConfirmEmailView):
    def get(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.confirm(self.request)
        return redirect(os.environ.get("FRONTEND_URL"))


class VerifyEmailView(VerifyEmailView):
    def get(self, request, *args, **kwargs):
        key = request.query_params.get("key")
        self.kwargs["key"] = key
        return self.post(request, *args, **kwargs)


@api_view(['POST'])
def resend_email_confirmation(request):
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    if user:
        send_email_confirmation(request, user)
    return Response({"detail": "Email sent if the user exists."})
