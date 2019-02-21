from rest_framework.decorators import api_view
from rest_framework.response import Response
from py_zipkin.zipkin import zipkin_span
from tracing.transport import SimpleHTTPTransportHandler



@api_view(['get'])
def get_results(_):
    with zipkin_span(
        host="zipkin",
        port=9411,
        span_name="get_results",
        service_name="frontend",
        transport_handler=SimpleHTTPTransportHandler(),
        sample_rate=100.0,
    ):
        return Response({'result': 42})
