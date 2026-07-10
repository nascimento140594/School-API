from django.shortcuts import render


def home(request):
    """
    Render the School API landing page.
    """
    return render(request, "home.html")
