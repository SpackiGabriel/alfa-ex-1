from rest_framework import serializers
from dashboard.models import Client, Module, Ticket

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'name']

class TicketSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), write_only=True, source='client'
    )

    module = ModuleSerializer(read_only=True)
    module_id = serializers.PrimaryKeyRelatedField(
        queryset=Module.objects.all(), write_only=True, source='module'
    )

    opening_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'id', 'title', 'client', 'client_id', 'module', 'module_id',
            'opening_date', 'closing_date'
        ]

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)
