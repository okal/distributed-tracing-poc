from rest_framework.decorators import api_view
from rest_framework.response import Response
from py_zipkin.zipkin import zipkin_span


@zipkin_span(
    host="zipkin",
    span_name="get_results",
    service_name="frontend",
    transport_handler=None
)
@api_view(['get'])
def get_results(_):
    return Response({'result': 42})
