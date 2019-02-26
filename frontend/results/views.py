from rest_framework.decorators import api_view
from rest_framework.response import Response
from requests import get
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
    ) as zipkin_context:
        headers = {
            "X-B3-Trace-Id": zipkin_context.zipkin_attrs.trace_id,
            "X-B3-Span-Id": zipkin_context.zipkin_attrs.trace_id,
            "X-B3-Parent-Span-Id": zipkin_context.zipkin_attrs.trace_id,
            "X-B3-Sampled": 1
        }
        response = get("http://io-bound:3000/lookup/index", headers=headers)
        return Response(response.json())
