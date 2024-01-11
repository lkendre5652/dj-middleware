from django.shortcuts import render, HttpResponse

def Home(request):
    print('This is the view!!')    
    return render(request, 'common/file.html')