from django.db import models

class Client(models.Model):
    class Meta:
        db_table = 'CLIENT'

    id = models.AutoField(primary_key = True, db_column = 'ID')
    name = models.CharField(max_length = 255, db_column = 'NAME')

class Module(models.Model):
    class Meta:
        db_table = 'MODULE'

    id = models.AutoField(primary_key = True, db_column = 'ID')
    name = models.CharField(max_length = 255, db_column = 'NAME')

class Ticket(models.Model):
    class Meta:
        db_table = 'TICKET'

    id = models.AutoField(primary_key = True, db_column = 'ID')
    title = models.CharField(max_length = 255, db_column = 'TITLE')
    client = models.ForeignKey(Client, on_delete = models.CASCADE, db_column = 'FK_ID_CLIENT')
    module = models.ForeignKey(Module, on_delete = models.CASCADE, db_column = 'FK_ID_MODULE')
    opening_date = models.DateTimeField(auto_now_add = True, db_column = 'OPENING_DATE')
    closing_date = models.DateTimeField(auto_now_add = False, null = True, db_column = 'CLOSING_DATE')
