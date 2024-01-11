# class based middleware
class MyMiddleWare():
    def __init__(self, get_response):
        self.get_response = get_response
        print('one time run')
    def __call__(self,request):
        print("before view")
        response = self.get_response(request)        
        print("after view")
        return response

