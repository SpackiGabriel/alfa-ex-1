from django.db import models

class Cliente(models.Model):
    class Meta:
        db_table = 'CLIENTE'

    id = models.AutoField(primary_key = True, db_column = 'ID')
    nome = models.CharField(max_length = 255, db_column = 'NOME')

class Modulo(models.Model):
    class Meta:
        db_table = 'MODULO'

    id = models.AutoField(primary_key = True, db_column = 'ID')
    nome = models.CharField(max_length = 255, db_column = 'NOME')

class Ticket(models.Model):
    class Meta:
        db_table = 'TICKET'

    id = models.AutoField(primary_key = True, db_column = 'ID')
    titulo = models.CharField(max_length = 255, db_column = 'TITULO')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, db_column = 'CODCLIENTE')
    modulo = models.ForeignKey(Modulo, on_delete = models.CASCADE, db_column = 'CODMODULO')
    data_abertura = models.DateTimeField(auto_now_add = True, db_column = 'DATAABERTURA')
    data_encerramento = models.DateTimeField(auto_now_add = True, db_column = 'DATAENCERRAMENTO')
