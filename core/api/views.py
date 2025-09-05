from django.http import HttpRequest
from django.http import HttpResponse


def index(_: HttpRequest) -> HttpResponse:
    """
    Returns a simple message when the user visits the site hosting the sitev4-backend API.
    """
    return HttpResponse("You're at jamie's site.")
