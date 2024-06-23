from rest_framework.decorators import api_view
from rest_framework.response import Response

from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


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
