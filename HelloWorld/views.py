from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    developed_by = 'Tejas Malik'
    friends = [
        "Hitesh",
        "Rohan",
        "Yash",
        "Devansh",
        "Harshit"
    ]

    context = {
        'developer': developed_by,
        'friends': friends
    }
    response = render(request, 'HelloWorld\index.html', context)

    return response

