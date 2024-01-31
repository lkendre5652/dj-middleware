from django.http import HttpResponse

class Process_view_middleware:
    def __init__(self,get_response):        
        self.get_response = get_response
        print('One Time Call')
    def __call__(self,request):
        response = self.get_response(request)
        return response
    # def process_view(request, *args, **kwargs):
    #     print('This is Process view- before view')
    #     # return HttpResponse('Before view') # if it not return None then view will not call
    #     return None
    
    # def process_exception(self,request, exception):
    #     msg = exception
    #     classname = exception.__class__.__name__
    #     data ={
    #        msg: msg,
    #        classname : classname
    #     }
    #     return HttpResponse(data)

    def process_template_response(self, request, response):
        print('Process template response view middleware')
        response.context_data['name'] = 'Laxman'
        return response