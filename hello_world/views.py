from django.shortcuts import render
from hello_world.models import Table_1, Table_2

# Create your views here.
def hello_world(request):
    table_1 = Table_1.objects.all()
    return render(request,"hello_world.html", {"table_1" : table_1})