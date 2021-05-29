from django.shortcuts import HttpResponse
from django.utils import timezone


def hello(request):
    return HttpResponse(f'Hello world! Now is {timezone.now()}')