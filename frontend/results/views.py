from rest_framework.decorators import api_view
from rest_framework.response import Response
from requests import get
from py_zipkin.zipkin import zipkin_span
from tracing.transport import SimpleHTTPTransportHandler
from tracing.utils import generate_zipkin_headers


@api_view(['get'])
def get_results(_):
    with zipkin_span(
        host="zipkin",
        port=9411,
        span_name="get_results",
        service_name="frontend",
        transport_handler=SimpleHTTPTransportHandler(),
        sample_rate=100.0,
    ) as zipkin_context:
        lookup_headers = generate_zipkin_headers(zipkin_context)
        heavy_headers = generate_zipkin_headers(zipkin_context)
        lookup_response = get("http://io-bound:3000/lookup/index", headers=lookup_headers).json()
        heavy_response = get("http://cpu-bound:8080/result/", headers=heavy_headers).json()
        return Response({**lookup_response, **heavy_response})
