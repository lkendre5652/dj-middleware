from django.shortcuts import render, HttpResponse
def func_middelware(get_response):
    print("This is the one time.")
    def myfunc(request):
        print("before")
        resp = get_response(request)
        print("before")
        return resp
    return myfunc
