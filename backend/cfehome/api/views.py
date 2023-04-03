from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

# echo get data
def api_home_old1(request,*args,**kwargs):
#     # request -> http request from django
#     # sent json request can be found in request.body

#     body = request.body  #we receive a btye string od JSON data and thats it
    resp = {}
#     try:
#         resp = json.loads(body) #byte string of json data -> python dict
#     except:
#         pass

#     resp['params'] = dict(request.GET)
#     resp['headers'] = dict(request.headers) #httpheaders is not JSON serialable, thats why we use dict
#     resp['content_type'] = request.content_type
    return JsonResponse(resp)

#django model instance as API resource
def api_home(request,*args,**kwargs):
    model_data =   Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','price'])
        #here we are converting a model instance(model_data) into a python dict(data) which becomes jsonresponse
        #this is also known as serialization
    return JsonResponse(data)