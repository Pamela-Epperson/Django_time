from django.shortcuts import render, HttpResponse

# def index(request):
#     return HttpResponse("Welcome to Django")

from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%b %d, %Y %I:%M %p", gmtime())
        }
    return render(request,'index.html', context)

