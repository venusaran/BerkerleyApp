import redis
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CountSerializer, ErrorSerializer

# Establishing Connection with Redis
r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


@api_view(['GET'])
def visit_count(request):
    if request.method == 'GET':
        try:
            # Increment the counter value with 1 for each request
            visit_counter = r.incr('visit_count', 1)
            res = {'visit_count': visit_counter}
            # Serializing
            serializer = CountSerializer(res)
            return Response(serializer.data)
        except Exception as e:
            err = {'error': e}
            serializer = ErrorSerializer(err)
            return Response(serializer.data)
