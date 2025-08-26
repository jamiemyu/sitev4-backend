from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at jamie's coaching site.")