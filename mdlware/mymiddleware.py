# middleware creations
# register/active middleware in settings.py file like appname.middleware_file.function_name
def My_middleware(get_response):
    print("One time initialization")
    def my_func(request):
        print('Before view')
        response = get_response(request)
        print('After view')
        return response
    return my_func