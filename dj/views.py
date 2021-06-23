import random

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string



def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        print("post success")
        formulas = [{
            "id": i,
            "confidence": 1.00,
            "x": random.randint(1, 1000),
            "y": random.randint(1, 1000),
            "width": random.randint(1, 1000),
            "height": random.randint(1, 1000),
            "text": "1+1=2",
        } for i in range(13)]
        html = render_to_string('formula_details.html', {'formulas': formulas})
        return HttpResponse(html)

