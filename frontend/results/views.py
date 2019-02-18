from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['get'])
def get_results(_):
    return Response({'result': 42})

