from django.http import HttpResponse
def home(_request):
    return HttpResponse("hello wordl")

def about(_request):
    return HttpResponse("hello about")