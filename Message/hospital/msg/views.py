from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hospital(request):
    html_content = """
    <html>
        <head>
            <title>Hospital</title>
        </head>
        <body>
            <h1>Welcome to our hospital.<h1>
           <h3>Departments</h3>
            <ul>
                <li>Surgery</li>
                <li>Neurology</li>
                <li>Emergency</li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html_content)

