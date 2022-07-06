from django.shortcuts import render

def index(request):
    return render(request, 'index.html',{

    })

def instructions(request):
    return render(request, 'instructions.html',{

    })

def routes(request):
    return render(request, 'routes.html',{

    })