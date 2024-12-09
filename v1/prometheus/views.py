from prometheus_client import Counter, generate_latest
from django.http import HttpResponse


REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests')

def metrics_view(request):
    REQUEST_COUNT.inc()
    return HttpResponse(generate_latest(), content_type='text/plain')
