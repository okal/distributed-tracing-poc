from py_zipkin.util import generate_random_64bit_string


def generate_zipkin_headers(zipkin_context):
    return {
        "X-B3-TraceId": zipkin_context.zipkin_attrs.trace_id,
        "X-B3-ParentSpanId": zipkin_context.zipkin_attrs.span_id,
        "X-B3-SpanId": generate_random_64bit_string(),
        "X-B3-Sampled": '1'
    }
