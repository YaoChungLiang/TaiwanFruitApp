from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request,*args, **kargs):
    print(*args, **kargs)
    print(request)
    print(request.user)
    #return HttpResponse("<h1> Home Page </h1>")  
    return render(request, "home.html", {})  # the third one is a context
    
def contact_view(request,*args, **kargs):
    #return HttpResponse("<h1> Contact </h1>")  
    return render(request, "contact.html", {})  # the third one is a context

def aboutMe_view(request,*args, **kargs):
    #return HttpResponse("<h1> about ME </h1>")  
    my_context = {
        "my_text" : "This is about the Supermarket",
        "my_number" : 4252192910,
        "my_list" : [123,25,21]
    }
    return render(request, "aboutMe.html", my_context)  # the third one is a context

def Ann_view(request,*args, **kargs):
    return HttpResponse("<h1> hi Ann </h1>")  