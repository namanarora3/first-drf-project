from django.http import JsonResponse
import json

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