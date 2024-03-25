from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Importing JsonResponse is unnecessary as it's not used in the code

"""to deploy"""


def index(request):
    """
    Render the index.html template.

    Parameters:
    - request: HttpRequest object

    Returns:
    - Rendered template response
    """
    return render(request, "index.html")


"""to deploy"""


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom token obtain pair serializer.

    Extends TokenObtainPairSerializer to include custom claims in the token payload.
    """

    @classmethod
    def get_token(cls, user):
        """
        Override get_token method to include custom claims in the token.

        Parameters:
        - user: User object

        Returns:
        - Token with custom claims
        """
        token = super().get_token(user)

        # Add custom claims
        token["email"] = (user.email,)
        token["username"] = (user.username,)
        token["first_name"] = user.first_name
        token["admin"] = user.is_staff

        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Custom token obtain pair view.

    Extends TokenObtainPairView to use the custom token serializer.
    """
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def getRoutes(request):
    """
    Get available API routes.

    This endpoint returns a list of available API routes.

    Parameters:
    - request: HttpRequest object

    Returns:
    - Response containing a list of available routes
    """
    routes = [
        "/api/token",         # Endpoint to obtain a token
        "/api/token/refresh",  # Endpoint to refresh a token
        "/api/token/revoke",  # Endpoint to revoke a token
    ]
    return Response(routes)
