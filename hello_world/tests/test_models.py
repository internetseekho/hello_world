from django.test import TestCase
from hello_world.models import Table_1, Table_2

class TestModels(TestCase):
    
    def setUpTable1(self):
        self.tab1_obj1 = Table_1.objects.create( field_1 = "I am here" )
    
    def setUpTable2(self):
        self.tab2_obj1 = Table_2.objects.create( field_2   = "I am here" )
        