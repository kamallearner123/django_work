from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Render the index page for the AI application.
    """
    return render(request, "ai/index.html", {"message": "Welcome to the AI Application! Blogs"})
    # return HttpResponse("Welcome to the AI Application!")