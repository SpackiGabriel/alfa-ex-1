from django.db import models

class Client(models.Model):
    """
    Represents a client in the system.

    Attributes:
        id (AutoField): The primary key for the client.
        name (CharField): The name of the client.
    """

    class Meta:
        db_table = 'CLIENT'

    id = models.AutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=255, db_column='NAME')

class Module(models.Model):
    """
    Represents a module in the system.

    Attributes:
        id (AutoField): The primary key for the module.
        name (CharField): The name of the module.
    """

    class Meta:
        db_table = 'MODULE'

    id = models.AutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=255, db_column='NAME')

class Ticket(models.Model):
    """
    Represents a ticket in the system.

    Attributes:
        id (AutoField): The primary key of the ticket.
        title (CharField): The title of the ticket.
        client (ForeignKey): The foreign key to the client associated with the ticket.
        module (ForeignKey): The foreign key to the module associated with the ticket.
        opening_date (DateTimeField): The date and time when the ticket was opened.
        closing_date (DateTimeField): The date and time when the ticket was closed (nullable).
    """

    class Meta:
        db_table = 'TICKET'

    id = models.AutoField(primary_key=True, db_column='ID')
    title = models.CharField(max_length=255, db_column='TITLE')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='FK_ID_CLIENT')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, db_column='FK_ID_MODULE')
    opening_date = models.DateTimeField(auto_now_add=True, db_column='OPENING_DATE')
    closing_date = models.DateTimeField(auto_now_add=False, null=True, db_column='CLOSING_DATE')
