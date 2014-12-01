from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from hunts.models import Hunt, Business, User
from hunts.serializers import HuntSerializer, BusinessSerializer, UserSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def hunt_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        hunts = Hunt.objects.all()
        serializer = HuntSerializer(hunts, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HuntSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        hunt = Hunt.objects.get(pk=pk)
    except Hunt.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HuntSerializer(hunt)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HuntSerializer(hunt, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        hunt.delete()
        return HttpResponse(status=204)
