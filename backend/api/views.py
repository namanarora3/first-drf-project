from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

'''echo get data
def api_home(request,*args,**kwargs):
    # request -> http request from django
    # sent json request can be found in request.body
    body = request.body  #we receive a btye string od JSON data and thats it
    resp = {}
    try:
        resp = json.loads(body) #byte string of json data -> python dict
    except:
        pass
    resp['params'] = dict(request.GET)
    resp['headers'] = dict(request.headers) #httpheaders is not JSON serialable, thats why we use dict
    resp['content_type'] = request.content_type
    return JsonResponse(resp)
'''

'''django model instance as API resource using DRF
@api_view(['GET'])
def api_home(request,*args,**kwargs):
    model_data =   Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','price'])
        #here we are converting a model instance(model_data) into a python dict(data) which becomes jsonresponse
        #this is also known as serialization
    return Response(data)
'''
'''
# model serializer starting
@api_view(['GET']) # API devorator for model
def api_home(request,*args,**kwargs):
    instance =   Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id','price','sale_price'])
        #here we are converting a model instance(model_data) into a python dict(data) which becomes jsonresponse
        #this is also known as serialization
        data = ProductSerializer(instance).data
    return Response(data)
'''

# ingesting data, VERIFYING IT USING SERIALISER AND PUSHING IT INTO DB
@api_view(["POST"])
def api_home(request,*args, **kwargs):
    serialiser = ProductSerializer(data = request.data)
    if(serialiser.is_valid(raise_exception=True)):
        print(serialiser.validated_data)
        content = serialiser.validated_data.get("content") or None
        title = serialiser.validated_data.get("title")
        if content is None:
            content = title
        # serializer.save pushes the content into db
        serialiser.save(content = content)
        return Response(serialiser.data)
    # return Response({"error": "serialiser not valid"})
