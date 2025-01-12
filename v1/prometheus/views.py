from django.http import HttpResponse, HttpResponseServerError

try:
    from prometheus_client import Counter, generate_latest

    REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests')

    def metrics_view(request):
        REQUEST_COUNT.inc()
        return HttpResponse(generate_latest(), content_type='text/plain')

except (ImportError, ModuleNotFoundError):
    Counter = None
    generate_latest = None

    def metrics_view(request):
        return HttpResponseServerError("Prometheus metrics are not available. Install prometheus_client.")

