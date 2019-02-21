from py_zipkin.transport import BaseTransportHandler
from requests import post


class SimpleHTTPTransportHandler(BaseTransportHandler):
    def get_max_payload_bytes(self):
        return None

    def send(self, payload):
        post(
            'http://zipkin:9411/api/v1/spans',
            data=payload,
            headers={'Content-Type': 'application/x-thrift'}
        )