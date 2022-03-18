import random
from datetime import datetime
import django

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from firstapp.models import Student


def my_first_view(request):

    return HttpResponse(f'''
    <form method="POST">
       <input name="name"/>
       <input type="submit"/>
    </form>
    name: {request.POST.get("name")}
    ''')
