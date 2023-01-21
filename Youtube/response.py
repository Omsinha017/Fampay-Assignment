from django.http.response import JsonResponse

def init_response(res_str=None, data=None):
    response = {}
    response['res_str'] = ""
    response['res_data'] = {}
    if res_str is not None:
        response['res_str'] = res_str
    if data is not None:
        response['res_data'] = data
    return response
 
def send_200(data, res_str=''):
    if res_str:
        data['res_str'] = res_str
    return JsonResponse(data, status=200)

def send_201(data, res_str=''):
    if res_str:
        data['res_str'] = res_str
    return JsonResponse(data, status=201)


def send_400(data, res_str=''):
    if res_str:
        data['res_str'] = res_str
    return JsonResponse(data, status=400)
