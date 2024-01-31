from django.shortcuts import HttpResponse
import json
from .models import Student
# def MYFUC_MIDDLEWARE(get_response):
#     print('one time initializations')
#     def mdlFunc(request):
#         print('before view 201')
#         resp = get_response(request)
#         print('after view 200')
#         return resp
#     return mdlFunc

class MYFUC_MIDDLEWARE:
    def __init__(self,get_response):
        self.get_response = get_response
        print('First Time Initializations cls')
    def __call__(self, request):
        print('First')
        resp = self.get_response( request)
        print('Last')
        return resp
    def process_view(self, request, *args, **kwargs):
        print('process view')
        studData = Student.objects.all()
        data = {
            'name' : 'laxman kendre'
        }
        jsonData = []
        for items in studData:
            jsonData.append( {'id': items.id, 'name':items.name } )        
        return HttpResponse(f"{json.dumps(jsonData)}")
