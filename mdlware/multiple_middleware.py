class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Brother one time brother initialization")
    def __call__(self,request):
        print('Brother before view')
        response = self.get_response(request)
        print('Brother after view')
        return response

class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('Father one time father')
    def __call__(self,request):
        print('Father before view ')
        response = self.get_response(request)
        print('Father after view ')
        return response

class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('Mother one time ')
    def __call__(self,request):
        print('Mother before view')
        resp = self.get_response(request)
        print('Mother after view')
        return resp
