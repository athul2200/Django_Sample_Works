from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def college(request):
    html_content = """
    <html>
        <head>
            <title>My college</title>
        </head>
        <body>
            <h1>Welcome to our college.</h1>
            <h3>Branches</h3>
            <ul>
                <li>CT</li>
                <li>EL</li>
                <li>EC</li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html_content)
