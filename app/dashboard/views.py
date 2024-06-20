from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dashboard.models import Ticket
from dashboard.serializers import TicketSerializer
from dashboard.utils import count_by, group_by


class DashboardView(APIView):
    def get(self, request):
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        if not month or not year:
            return Response(
                {'error': 'Mês e ano são parâmetros obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            tickets = Ticket.objects.filter(opening_date__month=month, opening_date__year=year)
        except ValueError:
            return Response(
                {'error': 'Formato de mês ou ano inválido.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TicketSerializer(tickets, many=True)

        count_by_client = count_by(group_by(lambda item: item['client']['name'], serializer.data))
        count_by_module = count_by(group_by(lambda item: item['module']['name'], serializer.data))

        return Response(
            {
                'tickets': serializer.data,
                'count_by_client': count_by_client,
                'count_by_module': count_by_module
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = TicketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'ticket': serializer.data,
                    'message': 'Ticket aberto com sucesso.'
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
