from django.shortcuts import render

class prs_tmp_resp:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time initialization")
    def __call__(self, request):
        print("before")
        resp = self.get_response(request)
        print("before")
        return resp
    def process_template_response(self,request,response):
        response.context_data['name'] = 'Laxman'
        return response