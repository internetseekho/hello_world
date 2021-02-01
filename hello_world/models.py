from django.db import models

# Create your models here.

class Table_2 ( models.Model ):
    table_2_id = models.IntegerField()
    field_2    = models.CharField(max_length=255)
    
    class Meta:
        db_table = "table_2"

    def __str__(self):
        return self.field_2

class Table_1 (models.Model):
    table_1_id = models.IntegerField()
    field_1    = models.CharField(max_length=255)
    table_2    = models.ForeignKey(Table_2, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "table_1"

    def __str__(self):
        return self.field_1