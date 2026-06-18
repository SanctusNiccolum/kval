from django.shortcuts import redirect, render
from django.http import HttpResponse


def test(request):
    return HttpResponse("OK")


def error_404_view(request, exception=None):
    return render(request, "404.html")