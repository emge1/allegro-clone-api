from django.http import HttpResponse, HttpResponseServerError
from prometheus_client import Counter, generate_latest


def metrics_view(request):
    return HttpResponse(generate_latest(), content_type='text/plain')
