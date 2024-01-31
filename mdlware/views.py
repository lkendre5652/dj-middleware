from django.shortcuts import render, HttpResponse
# from django.template.response import TemplateResponse
from   django.template.response import TemplateResponse

def Home(request):
    # print(10/0)
    print('This is the view!!')    
    context = {
        'name': 'test'
    }
    # return TemplateResponse(request, 'common/file.html',context)
    return TemplateResponse(request, 'common/file.html', context)